# Profile maintenance

The profile README, SVG artwork and LinkedIn cards are maintained in this repository.

## LinkedIn cards

Verified original public posts are stored in `data/linkedin-posts.json`, newest first, up to three. Use each canonical share/post ID and a clean permalink without tracking parameters. Titles and summaries describe the post; they do not endorse offers or copy private content.

Render cards with:

```bash
python scripts/render_linkedin.py
```

The README links and image version IDs live between `LINKEDIN-POSTS:START` and `LINKEDIN-POSTS:END`. Keep those IDs synchronized with the JSON.

A Codex follow-up in the owner's local chat is configured to check for new public posts every six hours and update this section when posts change. It needs the local computer and connected browser available. This repository does not contain a LinkedIn API token or a LinkedIn webhook. If the source cannot be verified, keep the last verified cards.

## Artwork and statistics

The illustrated pipeline is decorative and does not report real CI runs. SVGs support reduced-motion preferences. Live statistics are provided by external GitHub statistics services and may be cached or temporarily unavailable.

## Public links

Use only public source repositories in the project showcase. Link private projects to an existing public portfolio rather than exposing private repository details. Preserve the original design credit in the README.
