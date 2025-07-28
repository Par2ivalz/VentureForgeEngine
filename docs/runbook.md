# Operational Run‑book

This run‑book describes the routine procedures and tasks required to operate the VentureForge Engine.

## Daily tasks (automated)

* **Content generation:**  Run the writer and media sub‑agents to generate fresh scripts, images and videos for both niches.  Queue the content in the scheduler.
* **Publishing:**  Use n8n/Zapier flows to post queued content to YouTube/Shorts and update the digital product storefront.  Each post should include relevant product links and calls‑to‑action.
* **Analytics pull:**  Fetch metrics from YouTube Analytics, Gumroad/Stripe and the website via APIs.  Store the data in the Airtable/Notion base.
* **Optimisation algorithm:**  Execute the multi‑armed bandit or other optimisation script to analyse performance data.  Adjust topic selection and posting times based on the results.

## Weekly tasks (manual ~15 min)

* **Review KPI dashboard:**  Inspect the automatically generated KPI report to check revenue, click‑through rates, conversion rates and subscriber growth.
* **Approve major pivots:**  The optimisation algorithm may suggest new topics or products; approve any substantial changes.
* **Respond to queries:**  Address any customer inquiries or comments that cannot be handled automatically.

## Monthly tasks

* **Scaling:**  Once the monthly profit exceeds the target, initiate a clone of the pipeline into a new niche (e.g., health & wellness).
* **Compliance audit:**  Verify that content and products comply with platform terms of service and legal requirements.
* **Backup:**  Ensure repository, databases and assets are backed up.
