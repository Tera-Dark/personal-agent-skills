# Anima Tag Index

Web-first Anima 1.0 lookup data for Tera-Dark's personal image prompt system.

Source: `ShiroEirin/comfyui-good-anima/danbooru-tags/anima-1.0.csv`

Runtime policy: exact canonical and exact alias matches are verifiable; fuzzy/candidate matches are never directly promoted to hard tags. Missing concepts remain natural language.

Files are sharded by the first normalized character so a web model can fetch a small text file instead of the full dataset.

This directory is data only. Prompt-writing policy lives in the Anima compiler.
