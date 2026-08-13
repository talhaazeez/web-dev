# Form Ending response fix

The workflow previously sent Form Trigger executions to `Respond to Webhook`, which is unsupported for n8n Form Trigger workflows. The live workflow now sets all three Form Trigger nodes to `responseMode: lastNode` and routes their outputs through n8n Form nodes configured with `operation: completion` (Form Ending).

Form submissions use these paths:

- `download`: `Form Ending - Markdown Download` returns the Markdown binary file.
- `drive`: `Upload Form Markdown to Google Drive` followed by `Form Ending - Google Drive Confirmation`.

Webhook/API submissions remain on the original `Choose Google Drive or Download` branch and use `Respond to Webhook` for programmatic downloads.

Pinned verification tests completed successfully:

- Form branch: execution `118`.
- Webhook branch: execution `119`.

The workflow remains inactive.
