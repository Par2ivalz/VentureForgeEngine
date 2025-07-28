# Architecture

The VentureForge Engine consists of several modular components that work together to generate revenue with minimal human oversight.

![architecture-diagram](architecture_diagram.png)

1. **Content ideation & generation:**  A writer sub‑agent researches keywords, trends and SEO topics for the chosen niches and drafts scripts/articles with metadata.  A media sub‑agent generates images, voice‑overs and video clips using generative tools (DALL·E, Pika, ElevenLabs).  The generated assets are stored in a content queue.
2. **Scheduler & publishing:**  An automation layer (n8n/Zapier plus ChatGPT Tasks) publishes content across platforms on a set cadence (e.g., eight posts per day).  Publishing targets include YouTube/Shorts, the digital product storefront and (later) a programmatic SEO blog.
3. **Monetisation:**  A digital products marketplace built on Gumroad or Shopify hosts AI prompt packs, eco planners, templates and other downloadable goods.  The YouTube channel integrates affiliate links and promotes these products in video descriptions.
4. **Analytics & feedback loop:**  A collector gathers performance metrics from YouTube Analytics, the storefront (Stripe/Gumroad) and web analytics.  These metrics feed into a self‑optimising algorithm that adjusts topics, posting schedules and product offerings to maximise revenue.
5. **Task orchestration:**  All components are orchestrated via scheduled tasks (ChatGPT Tasks or cronjobs) defined in a workflow manager (n8n).  This enables the system to run continuously with less than 15 minutes per week of manual input.

The architecture is designed to be **cloneable**: once the pipeline is stable and profitable, it can be duplicated into additional niches with minimal configuration.
