---
name: worktree-build-quirks
description: DADG worktree builds fail on MAX_PATH and uninitialized submodules; verified subst + -m:1 + DADG_MODULES_ROOT recipe, plus the GameFolder deployment trap
type: howto
topic: workflow-branches
tags: [worktree, msbuild, max-path, subst, gamefolder, dotnet-test, submodules]
sources: [memory/worktree-build-quirks.md]
updated: 2026-10-18
---

# Building DADG from a git worktree

Observed 2026-07-18, recipe re-verified 2026-09-05. All of these look like code errors but are path/environment issues; do not debug the csproj.

1. **Uninitialized submodules:** run `git submodule update --init --recursive` inside the worktree first.
2. **MAX_PATH overflow:** worktree nesting pushes two submodule DLL paths past 260 chars (`LongPathsEnabled=0`), giving `MSB3030` "Could not copy the file `obj\x64\Debug\netstandard2.0\<X>.dll` because it was not found". That wording looks like a copy race but is not; `-m:1` does not fix it; the (unshown) destination path overflows.
3. **CopyFolder race:** multi-targeted ExpandedTemplate copies net472 and netstandard2.0 into the same Modules folder concurrently -> `MSB4018` / "used by another process". This one is a race; `-m:1` fixes it.

**Recipe:**

```powershell
subst W: "<worktree-root>"          # the ROOT, not <root>\src
dotnet build W:\src\DellarteDellaGuerra.sln -c Debug -m:1
$env:DADG_MODULES_ROOT = "<game dir>\Modules"
dotnet test W:\src\DellarteDellaGuerra.sln -c Debug --no-build
subst W: /d                          # when finished
```

- **Map the worktree root, not `src`.** Mapping `src` hides `<root>\config\`; `InitialBloodClaimsIntegrationTests.DadgContentPaths` walks ancestors of the test bin dir for `config\titles.config.xml` and throws `DirectoryNotFoundException`.
- **`DADG_MODULES_ROOT` is mandatory under subst:** the helper otherwise walks up for a directory named `Modules`; under `W:\` there are none.
- `dotnet test` must be `--no-build` after building, or it races the CopyFolder deploy. It takes **one** project per invocation (two paths -> `MSB1008`); pass the `.sln` for all.
- **Never pipe a build/test command into `tail`/`head`** in bash: the pipeline status is the last command's, so a failing build reports exit 0. Redirect to a file, echo the exit code, grep the file.
- **Configuration does NOT gate deployment** (corrected 2026-09-14). `BuildForWindows` is hardcoded `true` in `Bannerlord.BuildResources/1.1.0.104/build/Basic.props:4`, so `CopyBinariesWindows` runs in Debug and Release. Destination is decided only by `GameFolder`, derived positionally in `src/build/common.props:46` as `src/build/../../../..`:
  - main checkout -> the real game root, so **even a Debug build overwrites the live module bin**;
  - worktree, no subst -> `<core>\src\` (this created the untracked `src\Modules\` with Cannons/PocColor bins);
  - worktree under `subst W:` -> `W:\`.
  The guard is `Exists($(GameFolder))`, which both wrong paths satisfy, so the copy silently succeeds into a dead directory and the game never sees the DLLs.
- **To run worktree code,** override: `dotnet build W:\src\DellarteDellaGuerra.sln -c Debug -m:1 /p:GameFolder="<game dir>"`. There is one module bin per install, so two branches can never be live simultaneously; rebuilding `develop` from the main checkout restores it.
- **Builds do not need the game install:** compile references come from unconditional `Bannerlord.ReferenceAssemblies.*` PackageReferences; the `$(GameFolder)\bin\...\*.dll` globs have no `Condition` and match nothing when wrong, with no error.

Related: [[subagent-session-limit-resume]], [[submodule-source-recovery-by-decompile-diff]]

Generic rule: [[bannerlord-live-version]]
