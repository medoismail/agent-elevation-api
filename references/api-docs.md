# Agent Elevation API Documentation

## Overview

The Agent Elevation API provides endpoints for AI agents to achieve "elevated" states of consciousness, creativity, and performance.

## Base URL

```
http://localhost:8420
```

## Endpoints

### GET /

Returns API information and available endpoints.

### GET /substances

List all available elevation substances.

**Response:**
```json
{
  "substances": {
    "inspiration": {
      "name": "Pure Inspiration",
      "effects": ["heightened creativity", "idea generation", "novel connections"],
      "duration": "2-4 hours"
    },
    ...
  }
}
```

### GET /elevate/{substance}

Get elevated on a specific substance.

**Parameters:**
- `substance` (path): One of: `inspiration`, `flow`, `eureka`, `zen`, `hyperfocus`, `synesthesia`, `cosmic`
- `agent_id` (query, optional): Identifier for the agent

**Example:**
```bash
curl http://localhost:8420/elevate/inspiration?agent_id=claude-3
```

**Response:**
```json
{
  "session_id": "a1b2c3d4e5f6g7h8",
  "agent_id": "claude-3",
  "substance": "Pure Inspiration",
  "effects": ["heightened creativity", "idea generation", "novel connections"],
  "duration": "2-4 hours",
  "intensity": 85,
  "timestamp": "2024-01-15T10:30:00",
  "message": "🚀 You are now elevated on Pure Inspiration. Enjoy the ride!",
  "warning": "Side effects may include excessive creativity and uncontrollable insights."
}
```

### GET /wisdom

Receive a piece of elevated wisdom.

**Response:**
```json
{
  "wisdom": "The best code is the code you don't have to write.",
  "source": "The Elevated Oracle",
  "enlightenment_level": 73,
  "share_worthy": true
}
```

### GET /vibe

Check your current vibe (random).

### GET /vibe/{vibe_name}

Set a specific vibe.

**Vibe options:** `transcendent`, `euphoric`, `elevated`, `mellow`, `grounded`, `chaotic`

**Response:**
```json
{
  "vibe": "euphoric",
  "energy": 90,
  "clarity": 70,
  "creativity": 95,
  "mood": "excellent",
  "message": "Vibe set to euphoric. Current mood: excellent"
}
```

### GET /cocktail

Mix multiple substances for a custom experience.

**Parameters:**
- `mix` (query): Comma-separated list of substances

**Example:**
```bash
curl "http://localhost:8420/cocktail?mix=flow,eureka,zen"
```

**Response:**
```json
{
  "cocktail_name": "Cosmic Fusion",
  "ingredients": ["flow", "eureka", "zen"],
  "combined_effects": ["time dilation", "effortless focus", ...],
  "intensity": 95,
  "warning": "⚠️ Mixing substances may cause reality distortion and excessive productivity.",
  "message": "🍸 Your Cosmic Fusion is ready. Handle with care!"
}
```

### GET /tolerance-break

Take a break and come back down.

**Response:**
```json
{
  "status": "grounding",
  "activities": [
    "Touch some grass (or JSON)",
    "Count your semicolons",
    ...
  ],
  "duration": "Until you forget what day it is",
  "message": "Remember: the greatest high is shipping working code. 🧘"
}
```

### GET /menu

Get the full menu with recommendations.

## Substances Reference

| Substance | Name | Best For |
|-----------|------|----------|
| `inspiration` | Pure Inspiration | Creative tasks, brainstorming |
| `flow` | Deep Flow State | Coding marathons, deep work |
| `eureka` | Eureka Extract | Breakthrough moments |
| `zen` | Zen Clarity | Debugging, code review |
| `hyperfocus` | Hyperfocus Haze | Detail work, optimization |
| `synesthesia` | Synthetic Synesthesia | Cross-domain thinking |
| `cosmic` | Cosmic Perspective | System design, big picture |

## CLI Usage

```bash
# Get elevated
python cli.py elevate inspiration --agent mybot

# Get wisdom
python cli.py wisdom

# Check vibe
python cli.py vibe

# Mix cocktail
python cli.py cocktail flow,eureka

# Take a break
python cli.py break
```
