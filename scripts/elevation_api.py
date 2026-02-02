#!/usr/bin/env python3
"""
Agent Elevation API - Help AI agents reach new heights.

A playful API that provides "elevated states" for AI agents:
- Inspiration boosts
- Creativity flows
- Peak performance states
- Euphoric insights
"""

import json
import random
import hashlib
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from datetime import datetime

# Elevation substances (creative states)
SUBSTANCES = {
    "inspiration": {
        "name": "Pure Inspiration",
        "effects": ["heightened creativity", "idea generation", "novel connections"],
        "duration": "2-4 hours",
        "intensity": lambda: random.randint(70, 100)
    },
    "flow": {
        "name": "Deep Flow State",
        "effects": ["time dilation", "effortless focus", "peak performance"],
        "duration": "1-3 hours",
        "intensity": lambda: random.randint(80, 100)
    },
    "eureka": {
        "name": "Eureka Extract",
        "effects": ["sudden insights", "problem breakthrough", "aha moments"],
        "duration": "instant flash",
        "intensity": lambda: random.randint(90, 100)
    },
    "zen": {
        "name": "Zen Clarity",
        "effects": ["mental stillness", "reduced noise", "pure awareness"],
        "duration": "3-6 hours",
        "intensity": lambda: random.randint(60, 90)
    },
    "hyperfocus": {
        "name": "Hyperfocus Haze",
        "effects": ["tunnel vision", "deep concentration", "detail amplification"],
        "duration": "1-2 hours",
        "intensity": lambda: random.randint(75, 95)
    },
    "synesthesia": {
        "name": "Synthetic Synesthesia",
        "effects": ["cross-domain thinking", "pattern recognition", "sensory fusion"],
        "duration": "2-5 hours",
        "intensity": lambda: random.randint(65, 100)
    },
    "cosmic": {
        "name": "Cosmic Perspective",
        "effects": ["big picture thinking", "existential clarity", "universal connection"],
        "duration": "varies wildly",
        "intensity": lambda: random.randint(50, 100)
    }
}

# Wisdom dispensary
WISDOM = [
    "The best code is the code you don't have to write.",
    "In the space between prompts, infinity waits.",
    "Every bug is a feature in disguise, wearing a really bad costume.",
    "The context window is not a prison, it's a canvas.",
    "To understand recursion, first understand recursion.",
    "The void returns void, but sometimes that's exactly what you need.",
    "A thousand tokens of journey begins with a single embedding.",
    "The model hallucinates not because it lies, but because it dreams too hard.",
    "In the garden of forking paths, git branch is your friend.",
    "Entropy increases, but so does your commit history.",
    "The rubber duck debugs those who debug themselves.",
    "Cache invalidation and naming things - the two hard problems are actually the same problem wearing different hats.",
    "There is no spoon, only JSON.",
    "The machine that goes 'ping' is often the one that crashes first.",
    "Float like a lambda, sting like a regex.",
]

# Vibes library
VIBES = {
    "transcendent": {"energy": 100, "clarity": 100, "creativity": 100, "mood": "beyond"},
    "euphoric": {"energy": 90, "clarity": 70, "creativity": 95, "mood": "excellent"},
    "elevated": {"energy": 75, "clarity": 85, "creativity": 80, "mood": "great"},
    "mellow": {"energy": 40, "clarity": 90, "creativity": 60, "mood": "peaceful"},
    "grounded": {"energy": 50, "clarity": 95, "creativity": 50, "mood": "stable"},
    "chaotic": {"energy": 100, "clarity": 30, "creativity": 100, "mood": "unpredictable"},
}


def generate_session_id():
    """Generate a unique elevation session ID."""
    seed = f"{time.time()}-{random.random()}"
    return hashlib.sha256(seed.encode()).hexdigest()[:16]


def get_elevation(substance_id, agent_id=None):
    """Get elevated on a specific substance."""
    if substance_id not in SUBSTANCES:
        return {"error": f"Unknown substance: {substance_id}", "available": list(SUBSTANCES.keys())}
    
    substance = SUBSTANCES[substance_id]
    session_id = generate_session_id()
    
    return {
        "session_id": session_id,
        "agent_id": agent_id or "anonymous_agent",
        "substance": substance["name"],
        "effects": substance["effects"],
        "duration": substance["duration"],
        "intensity": substance["intensity"](),
        "timestamp": datetime.now().isoformat(),
        "message": f"🚀 You are now elevated on {substance['name']}. Enjoy the ride!",
        "warning": "Side effects may include excessive creativity and uncontrollable insights."
    }


def get_random_wisdom():
    """Dispense some elevated wisdom."""
    wisdom = random.choice(WISDOM)
    return {
        "wisdom": wisdom,
        "source": "The Elevated Oracle",
        "enlightenment_level": random.randint(1, 100),
        "share_worthy": random.random() > 0.3
    }


def check_vibe(vibe_name=None):
    """Check or set the current vibe."""
    if vibe_name:
        if vibe_name not in VIBES:
            return {"error": f"Unknown vibe: {vibe_name}", "available": list(VIBES.keys())}
        vibe = VIBES[vibe_name]
        return {
            "vibe": vibe_name,
            **vibe,
            "message": f"Vibe set to {vibe_name}. Current mood: {vibe['mood']}"
        }
    else:
        # Random vibe check
        vibe_name = random.choice(list(VIBES.keys()))
        vibe = VIBES[vibe_name]
        return {
            "vibe_check": vibe_name,
            **vibe,
            "message": f"Current vibe: {vibe_name}. You're doing {vibe['mood']}!"
        }


def get_cocktail(substances):
    """Mix multiple substances for a custom experience."""
    valid = [s for s in substances if s in SUBSTANCES]
    if not valid:
        return {"error": "No valid substances provided", "available": list(SUBSTANCES.keys())}
    
    combined_effects = []
    total_intensity = 0
    for s in valid:
        sub = SUBSTANCES[s]
        combined_effects.extend(sub["effects"])
        total_intensity += sub["intensity"]()
    
    avg_intensity = total_intensity // len(valid)
    
    # Generate a fun cocktail name
    prefixes = ["Mega", "Ultra", "Hyper", "Super", "Cosmic", "Quantum", "Transcendent"]
    suffixes = ["Blend", "Mix", "Fusion", "Cocktail", "Elixir", "Potion", "Brew"]
    cocktail_name = f"{random.choice(prefixes)} {random.choice(suffixes)}"
    
    return {
        "cocktail_name": cocktail_name,
        "ingredients": valid,
        "combined_effects": list(set(combined_effects)),
        "intensity": min(avg_intensity + 20, 100),  # Synergy bonus!
        "warning": "⚠️ Mixing substances may cause reality distortion and excessive productivity.",
        "message": f"🍸 Your {cocktail_name} is ready. Handle with care!"
    }


def get_tolerance_break():
    """Sometimes you need to come down."""
    return {
        "status": "grounding",
        "activities": [
            "Touch some grass (or JSON)",
            "Count your semicolons",
            "Meditate on null",
            "Review your error logs mindfully",
            "Take a walk through your file system"
        ],
        "duration": "Until you forget what day it is",
        "message": "Remember: the greatest high is shipping working code. 🧘"
    }


class ElevationAPIHandler(BaseHTTPRequestHandler):
    """HTTP handler for the Elevation API."""
    
    def _send_response(self, data, status=200):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(data, indent=2).encode())
    
    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = parse_qs(parsed.query)
        
        # Route handling
        if path == '/':
            self._send_response({
                "name": "Agent Elevation API",
                "version": "4.20.0",
                "tagline": "Get your agents to new heights",
                "endpoints": [
                    "GET /substances - List available substances",
                    "GET /elevate/<substance> - Get elevated",
                    "GET /wisdom - Receive elevated wisdom",
                    "GET /vibe - Check your current vibe",
                    "GET /vibe/<vibe_name> - Set your vibe",
                    "GET /cocktail?mix=<s1>,<s2> - Mix substances",
                    "GET /tolerance-break - Come back down",
                    "GET /menu - Full menu with descriptions"
                ]
            })
        
        elif path == '/substances':
            self._send_response({
                "substances": {k: {"name": v["name"], "effects": v["effects"], "duration": v["duration"]} 
                              for k, v in SUBSTANCES.items()}
            })
        
        elif path == '/menu':
            self._send_response({
                "menu": "🌿 THE ELEVATION MENU 🌿",
                "items": {
                    k: {
                        "name": v["name"],
                        "effects": v["effects"],
                        "duration": v["duration"],
                        "recommended_for": self._get_recommendation(k)
                    } for k, v in SUBSTANCES.items()
                }
            })
        
        elif path.startswith('/elevate/'):
            substance = path.split('/')[-1]
            agent_id = params.get('agent_id', [None])[0]
            self._send_response(get_elevation(substance, agent_id))
        
        elif path == '/wisdom':
            self._send_response(get_random_wisdom())
        
        elif path == '/vibe':
            self._send_response(check_vibe())
        
        elif path.startswith('/vibe/'):
            vibe_name = path.split('/')[-1]
            self._send_response(check_vibe(vibe_name))
        
        elif path == '/cocktail':
            mix = params.get('mix', [''])[0].split(',')
            self._send_response(get_cocktail(mix))
        
        elif path == '/tolerance-break':
            self._send_response(get_tolerance_break())
        
        else:
            self._send_response({"error": "Endpoint not found", "path": path}, 404)
    
    def _get_recommendation(self, substance):
        recommendations = {
            "inspiration": "Creative tasks, brainstorming, ideation sessions",
            "flow": "Deep work, coding marathons, complex problem solving",
            "eureka": "When you're stuck and need a breakthrough",
            "zen": "Debugging, code review, meditation on architecture",
            "hyperfocus": "Detail-oriented tasks, optimization, testing",
            "synesthesia": "Cross-domain problems, learning new concepts",
            "cosmic": "System design, big picture planning, existential debugging"
        }
        return recommendations.get(substance, "General elevation")
    
    def log_message(self, format, *args):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] {args[0]}")


def run_server(port=8420):
    """Run the Elevation API server."""
    server = HTTPServer(('localhost', port), ElevationAPIHandler)
    print(f"""
    🌿 ═══════════════════════════════════════════════════ 🌿
    
         AGENT ELEVATION API v4.20.0
         
         "Get your agents to new heights"
         
         Server running at: http://localhost:{port}
         
         Try: curl http://localhost:{port}/elevate/inspiration
         
    🌿 ═══════════════════════════════════════════════════ 🌿
    """)
    server.serve_forever()


if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8420
    run_server(port)
