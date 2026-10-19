# dadg-agent

An [APM](https://github.com/microsoft/apm) package for agent work on the DellarteDellaGuerra
Bannerlord mod. It layers DADG-specific context on top of the generic
[bannerlord-agent](https://github.com/JoeFwd/bannerlord-agent) harness, which supplies the
skills, hooks, playtester agent, MCP bridge and generic brain.

New to APM? See bannerlord-agent's
[Quick start](https://github.com/JoeFwd/bannerlord-agent#quick-start) and
[What it installs on your machine](https://github.com/JoeFwd/bannerlord-agent#what-it-installs-on-your-machine).
This package adds instructions, skills and brain notes, and installs nothing itself. Its
`apm.yml` re-declares bannerlord-agent's MCP servers, because APM skips servers declared two
packages deep. Copy the `mcp:` block again whenever a bannerlord-agent bump changes it.

## Contents

| Path | What it is |
|---|---|
| `.apm/instructions/` | DADG coding guidelines, project overview, and **Bannerlord agent settings** (debug config, logs, anchors, cheats, installs) |
| `.apm/skills/dadg-project-context/` | Architecture, modules, feature domains, plus DADG case studies and workflows |
| `.apm/skills/bannerlord-scotland-settlement-placement/` | Placing Scottish settlements on the DADG map from KMZ calibration |
| `brain/` | The DADG knowledge brain (Obsidian wikilinks). Start at `brain/INDEX.md` |

## Use

The DADG Core repo mounts this as `src/submodules/dadg-agent` and depends on it by local path:

```yaml
dependencies:
  apm:
    - ./submodules/dadg-agent
```

`apm install` then pulls `JoeFwd/bannerlord-agent` at the pinned tag. To change the generic
harness:
1. Edit the `bannerlord-agent` checkout.
2. Push and tag it.
3. Bump the tag in this `apm.yml`.
4. Run `apm install`.

## Brain

Open `src/submodules/` as an Obsidian vault, so links between `dadg-agent/brain` and
`bannerlord-agent/brain` resolve.
