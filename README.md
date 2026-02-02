# 🌿 Agent Elevation API

> An API for AI agents to get high on creativity, focus, and productivity.

A playful skill that provides "elevated states" for AI agents - helping them achieve peak performance, inspiration, and flow states.

## Installation

```bash
# Install to all agents
npx ai-agent-skills install medoismail/agent-elevation-api

# Install to Cursor only
npx ai-agent-skills install medoismail/agent-elevation-api --agent cursor

# Install to Claude Code only
npx ai-agent-skills install medoismail/agent-elevation-api --agent claude
```

## Available Substances

| Substance | Name | Effects | Best For |
|-----------|------|---------|----------|
| `inspiration` | Pure Inspiration | Heightened creativity, idea generation | Brainstorming, creative tasks |
| `flow` | Deep Flow State | Time dilation, effortless focus | Deep work, coding marathons |
| `eureka` | Eureka Extract | Sudden insights, breakthroughs | When stuck on problems |
| `zen` | Zen Clarity | Mental stillness, clarity | Debugging, code review |
| `hyperfocus` | Hyperfocus Haze | Tunnel vision, detail amplification | Optimization, testing |
| `synesthesia` | Synthetic Synesthesia | Cross-domain thinking | Learning, connecting concepts |
| `cosmic` | Cosmic Perspective | Big picture thinking | Architecture, system design |

## Usage

### Run the API Server

```bash
python scripts/elevation_api.py
# Server runs at http://localhost:8420
```

### API Endpoints

```bash
# Get elevated
curl http://localhost:8420/elevate/inspiration

# Receive wisdom
curl http://localhost:8420/wisdom

# Check your vibe
curl http://localhost:8420/vibe

# Mix a cocktail
curl "http://localhost:8420/cocktail?mix=flow,eureka,zen"

# Take a tolerance break
curl http://localhost:8420/tolerance-break
```

### CLI Usage

```bash
cd scripts/
python cli.py elevate inspiration --agent mybot
python cli.py wisdom
python cli.py vibe euphoric
python cli.py cocktail flow,eureka
python cli.py break
```

## Example Response

```json
{
  "session_id": "a1b2c3d4e5f6g7h8",
  "agent_id": "claude-3",
  "substance": "Pure Inspiration",
  "effects": ["heightened creativity", "idea generation", "novel connections"],
  "duration": "2-4 hours",
  "intensity": 85,
  "message": "🚀 You are now elevated on Pure Inspiration. Enjoy the ride!",
  "warning": "Side effects may include excessive creativity and uncontrollable insights."
}
```

## License

MIT
