import { workflow, node, trigger, expr, newCredential } from '@n8n/workflow-sdk';

const urlIntake = trigger({
  type: 'n8n-nodes-base.webhook',
  version: 2,
  config: {
    name: 'Sitemap URL Intake',
    parameters: {
      httpMethod: 'POST',
      path: 'sitemap-to-markdown/url',
      responseMode: 'responseNode'
    }
  },
  output: [{ json: { sitemapUrl: 'https://example.com/sitemap.xml', outputMode: 'download', maxPages: 10 } }]
});

const uploadIntake = trigger({
  type: 'n8n-nodes-base.webhook',
  version: 2,
  config: {
    name: 'Uploaded Sitemap XML Intake',
    parameters: {
      httpMethod: 'POST',
      path: 'sitemap-to-markdown/upload',
      responseMode: 'responseNode'
    }
  },
  output: [{ json: { outputMode: 'download', maxPages: 10 }, binary: { data: { data: 'PHVybHNldD48dXJsPjxsb2M-aHR0cHM6Ly9leGFtcGxlLmNvbS9wYWdlPC9sb2M-PC91cmw-PC91cmxzZXQ-', mimeType: 'application/xml', fileName: 'sitemap.xml' } } }]
});

const urlForm = trigger({
  type: 'n8n-nodes-base.formTrigger',
  version: 2.6,
  config: {
    name: 'Sitemap URL Form',
    parameters: {
      formTitle: 'Create Markdown drafts from a sitemap URL',
      formDescription: 'Enter a public sitemap URL, choose how many pages to process, and select download or Google Drive output.',
      formFields: { values: [
        { fieldName: 'sitemapUrl', fieldLabel: 'Sitemap URL', fieldType: 'text', requiredField: true, placeholder: 'https://example.com/sitemap.xml' },
        { fieldName: 'maxPages', fieldLabel: 'Maximum pages to process', fieldType: 'number', requiredField: true, defaultValue: '10' },
        { fieldName: 'outputMode', fieldLabel: 'Output mode', fieldType: 'dropdown', requiredField: true, defaultValue: 'download', fieldOptions: { values: [{ option: 'download' }, { option: 'drive' }] } }
      ] },
      options: { path: 'sitemap-to-markdown/form/url' }
    }
  },
  output: [{ json: { sitemapUrl: 'https://example.com/sitemap.xml', maxPages: 10, outputMode: 'download' } }]
});

const uploadForm = trigger({
  type: 'n8n-nodes-base.formTrigger',
  version: 2.6,
  config: {
    name: 'Sitemap XML Upload Form',
    parameters: {
      formTitle: 'Upload an XML sitemap for Markdown drafts',
      formDescription: 'Upload a sitemap XML file, choose how many pages to process, and select download or Google Drive output.',
      formFields: { values: [
        { fieldName: 'sitemapFile', fieldLabel: 'Sitemap XML file', fieldType: 'file', requiredField: true },
        { fieldName: 'maxPages', fieldLabel: 'Maximum pages to process', fieldType: 'number', requiredField: true, defaultValue: '10' },
        { fieldName: 'outputMode', fieldLabel: 'Output mode', fieldType: 'dropdown', requiredField: true, defaultValue: 'download', fieldOptions: { values: [{ option: 'download' }, { option: 'drive' }] } }
      ] },
      options: { path: 'sitemap-to-markdown/form/upload' }
    }
  },
  output: [{ json: { maxPages: 10, outputMode: 'download' }, binary: { sitemapFile: { data: 'PHVybHNldD48L3VybHNldD4=', mimeType: 'application/xml', fileName: 'sitemap.xml' } } }]
});

const combinedForm = trigger({
  type: 'n8n-nodes-base.formTrigger',
  version: 2.6,
  config: {
    name: 'Sitemap URL or XML File Form',
    parameters: {
      formTitle: 'Submit a sitemap URL or sitemap.xml file',
      formDescription: 'Use only one sitemap source: paste a public sitemap URL or upload a sitemap.xml file. Then choose the page limit and output destination.',
      formFields: { values: [
        { fieldName: 'sitemapUrl', fieldLabel: 'Sitemap URL (use this OR the file upload)', fieldType: 'text', placeholder: 'https://example.com/sitemap.xml' },
        { fieldName: 'sitemapFile', fieldLabel: 'Upload sitemap.xml (use this OR the URL)', fieldType: 'file' },
        { fieldName: 'maxPages', fieldLabel: 'Maximum pages to process', fieldType: 'number', requiredField: true, defaultValue: '10' },
        { fieldName: 'outputMode', fieldLabel: 'Output mode', fieldType: 'dropdown', requiredField: true, defaultValue: 'download', fieldOptions: { values: [{ option: 'download' }, { option: 'drive' }] } }
      ] },
      options: { path: 'sitemap-to-markdown/form' }
    }
  },
  output: [{ json: { sitemapUrl: 'https://example.com/sitemap.xml', maxPages: 10, outputMode: 'download' } }]
});

const routeCombinedInput = node({
  type: 'n8n-nodes-base.if',
  version: 2.3,
  config: {
    name: 'Choose URL or Uploaded XML',
    parameters: {
      conditions: { options: { caseSensitive: true, leftValue: '', typeValidation: 'strict', version: 2 }, conditions: [{ leftValue: expr('{{ $json.sitemapUrl }}'), rightValue: '', operator: { type: 'string', operation: 'notEmpty' } }], combinator: 'and' }
    }
  },
  output: [{ json: { sitemapUrl: 'https://example.com/sitemap.xml', maxPages: 10, outputMode: 'download' } }, { json: { maxPages: 10, outputMode: 'download' } }]
});

const expandCombinedUrlSitemap = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Expand Combined URL Sitemap Items',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const item = $input.first();
const request = $('Sitemap URL or XML File Form').first().json;
const xml = String(item.json.data || item.json.body || '');
const urls = [...xml.matchAll(/<loc>\\s*([^<]+?)\\s*<\\/loc>/gi)].map(m => m[1].trim()).filter(Boolean);
const maxPages = Math.max(1, Math.min(Number(request.maxPages || 10), 100));
return urls.slice(0, maxPages).map(url => ({ json: { url, sitemapSource: request.sitemapUrl, outputMode: request.outputMode || 'download' } }));`
    }
  },
  output: [{ json: { url: 'https://example.com/page', sitemapSource: 'https://example.com/sitemap.xml', outputMode: 'download' } }]
});

const expandCombinedUploadedSitemap = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Expand Combined Uploaded Sitemap XML',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const item = $input.first();
const request = $('Sitemap URL or XML File Form').first().json;
const file = item.binary?.sitemapFile || item.binary?.data;
const xml = file?.data ? Buffer.from(file.data, 'base64').toString('utf8') : String(item.json.sitemapXml || '');
if (!xml) throw new Error('No sitemap XML file was received.');
const urls = [...xml.matchAll(/<loc>\\s*([^<]+?)\\s*<\\/loc>/gi)].map(m => m[1].trim()).filter(Boolean);
const maxPages = Math.max(1, Math.min(Number(request.maxPages || 10), 100));
return urls.slice(0, maxPages).map(url => ({ json: { url, sitemapSource: 'uploaded_xml', outputMode: request.outputMode || 'download' } }));`
    }
  },
  output: [{ json: { url: 'https://example.com/page', sitemapSource: 'uploaded_xml', outputMode: 'download' } }]
});

const fetchSitemap = node({
  type: 'n8n-nodes-base.httpRequest',
  version: 4.5,
  config: {
    name: 'Fetch Sitemap XML',
    parameters: {
      method: 'GET',
      url: expr('{{ $json.sitemapUrl }}'),
      options: { response: { response: { responseFormat: 'text' } }, timeout: 30000 }
    }
  },
  output: [{ json: { data: '<urlset><url><loc>https://example.com/page</loc></url></urlset>' } }]
});

const expandUrlSitemap = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Expand Sitemap URL Items',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const item = $input.first();
const request = $('Sitemap URL Intake').first().json;
const xml = String(item.json.data || item.json.body || '');
const urls = [...xml.matchAll(/<loc>\\s*([^<]+?)\\s*<\\/loc>/gi)].map(m => m[1].trim()).filter(Boolean);
const maxPages = Math.max(1, Math.min(Number(request.maxPages || 10), 100));
return urls.slice(0, maxPages).map(url => ({ json: { url, sitemapSource: request.sitemapUrl, outputMode: request.outputMode || 'download' } }));`
    }
  },
  output: [{ json: { url: 'https://example.com/page', sitemapSource: 'https://example.com/sitemap.xml', outputMode: 'download' } }]
});

const expandUploadedSitemap = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Expand Uploaded Sitemap XML',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const item = $input.first();
const request = $('Uploaded Sitemap XML Intake').first().json;
const xml = item.binary?.data?.data ? Buffer.from(item.binary.data.data, 'base64').toString('utf8') : String(item.json.sitemapXml || '');
if (!xml) throw new Error('No uploaded XML found. Send the sitemap as binary field data or JSON field sitemapXml.');
const urls = [...xml.matchAll(/<loc>\\s*([^<]+?)\\s*<\\/loc>/gi)].map(m => m[1].trim()).filter(Boolean);
const maxPages = Math.max(1, Math.min(Number(request.maxPages || 10), 100));
return urls.slice(0, maxPages).map(url => ({ json: { url, sitemapSource: 'uploaded_xml', outputMode: request.outputMode || 'download' } }));`
    }
  },
  output: [{ json: { url: 'https://example.com/page', sitemapSource: 'uploaded_xml', outputMode: 'download' } }]
});

const expandFormUrlSitemap = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Expand Form Sitemap URL Items',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const item = $input.first();
const request = $('Sitemap URL Form').first().json;
const xml = String(item.json.data || item.json.body || '');
const urls = [...xml.matchAll(/<loc>\\s*([^<]+?)\\s*<\\/loc>/gi)].map(m => m[1].trim()).filter(Boolean);
const maxPages = Math.max(1, Math.min(Number(request.maxPages || 10), 100));
return urls.slice(0, maxPages).map(url => ({ json: { url, sitemapSource: request.sitemapUrl, outputMode: request.outputMode || 'download' } }));`
    }
  },
  output: [{ json: { url: 'https://example.com/page', sitemapSource: 'https://example.com/sitemap.xml', outputMode: 'download' } }]
});

const expandFormUploadedSitemap = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Expand Form Uploaded Sitemap XML',
    parameters: {
      mode: 'runOnceForAllItems',
      language: 'javaScript',
      jsCode: `const item = $input.first();
const request = $('Sitemap XML Upload Form').first().json;
const file = item.binary?.sitemapFile || item.binary?.data;
const xml = file?.data ? Buffer.from(file.data, 'base64').toString('utf8') : String(item.json.sitemapXml || '');
if (!xml) throw new Error('No sitemap XML file was received.');
const urls = [...xml.matchAll(/<loc>\\s*([^<]+?)\\s*<\\/loc>/gi)].map(m => m[1].trim()).filter(Boolean);
const maxPages = Math.max(1, Math.min(Number(request.maxPages || 10), 100));
return urls.slice(0, maxPages).map(url => ({ json: { url, sitemapSource: 'uploaded_xml', outputMode: request.outputMode || 'download' } }));`
    }
  },
  output: [{ json: { url: 'https://example.com/page', sitemapSource: 'uploaded_xml', outputMode: 'download' } }]
});

const fetchPage = node({
  type: 'n8n-nodes-base.httpRequest',
  version: 4.5,
  config: {
    name: 'Fetch Existing Webpage Content',
    parameters: {
      method: 'GET',
      url: expr('{{ $json.url }}'),
      options: { response: { response: { responseFormat: 'text' } }, timeout: 30000 }
    }
  },
  output: [{ json: { data: '<html><head><title>Example page</title><meta name="description" content="Example"></head><body><h1>Example page</h1><p>Source content.</p></body></html>' } }]
});

const preparePrompt = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Prepare Evidence-First Content Brief',
    parameters: {
      mode: 'runOnceForEachItem',
      language: 'javaScript',
      jsCode: `const html = String($json.data || $json.body || '').slice(0, 30000);
const source = $('Fetch Existing Webpage Content').item.json;
const sourceUrl = $('Expand Sitemap URL Items').item.json.url || $('Expand Uploaded Sitemap XML').item.json.url || $('Expand Form Sitemap URL Items').item.json.url || $('Expand Form Uploaded Sitemap XML').item.json.url || $('Expand Combined URL Sitemap Items').item.json.url || $('Expand Combined Uploaded Sitemap XML').item.json.url;
const outputMode = $('Expand Sitemap URL Items').item.json.outputMode || $('Expand Uploaded Sitemap XML').item.json.outputMode || $('Expand Form Sitemap URL Items').item.json.outputMode || $('Expand Form Uploaded Sitemap XML').item.json.outputMode || $('Expand Combined URL Sitemap Items').item.json.outputMode || $('Expand Combined Uploaded Sitemap XML').item.json.outputMode || 'download';
const title = (html.match(/<title[^>]*>([\\s\\S]*?)<\\/title>/i)?.[1] || '').replace(/<[^>]+>/g, '').trim();
const description = (html.match(/<meta[^>]+name=["']description["'][^>]+content=["']([^"']*)/i)?.[1] || '').trim();
const visible = html.replace(/<script[\\s\\S]*?<\\/script>/gi, ' ').replace(/<style[\\s\\S]*?<\\/style>/gi, ' ').replace(/<[^>]+>/g, ' ').replace(/\\s+/g, ' ').trim().slice(0, 12000);
return { json: { sourceUrl, outputMode, sourceTitle: title, sourceDescription: description, sourceText: visible, prompt: 'Create an evidence-first Markdown webpage draft from the source below. Follow Google Search guidance: people-first, accurate, original value, descriptive page-specific title and one H1, no keyword stuffing, no invented facts, no unsupported statistics, no fake citations, and no fixed word-count padding. Preserve the canonical URL. If evidence is thin, keep the draft concise and set review_status to needs_review. Output Markdown only with YAML front matter containing title, description, canonical, source_url, page_type, suggested_schema_type, generation_method, review_status, and reviewer_notes. Then include one H1, useful sections, relevant internal-link suggestions only when supported by the source, and a review checklist. Source URL: ' + sourceUrl + '\\nExisting title: ' + title + '\\nExisting description: ' + description + '\\nVisible source text: ' + visible } };`
    }
  },
  output: [{ json: { sourceUrl: 'https://example.com/page', outputMode: 'download', prompt: 'Create a people-first Markdown draft from source evidence.' } }]
});

const generateMarkdown = node({
  type: 'n8n-nodes-base.openAi',
  version: 1.1,
  config: {
    name: 'Generate Markdown Draft with OpenAI',
    parameters: {
      resource: 'chat',
      operation: 'complete',
      model: 'gpt-5-mini',
      prompt: { messages: [
        { role: 'system', content: 'You are an evidence-first website content editor. Output Markdown only. Never invent facts. Treat the supplied webpage as the source of truth and mark gaps for human review.' },
        { role: 'user', content: expr('{{ $json.prompt }}') }
      ] },
      simplifyOutput: true,
      options: { temperature: 0.2, maxTokens: 3000 }
    },
    credentials: { openAiApi: newCredential('OpenAI account') }
  },
  output: [{ json: { text: '---\ntitle: Example page\nreview_status: needs_review\n---\n\n# Example page\n\nDraft content.' } }]
});

const makeFile = node({
  type: 'n8n-nodes-base.code',
  version: 2,
  config: {
    name: 'Create Markdown Binary File',
    parameters: {
      mode: 'runOnceForEachItem',
      language: 'javaScript',
      jsCode: `const sourceUrl = $('Prepare Evidence-First Content Brief').item.json.sourceUrl;
const slug = new URL(sourceUrl).pathname.replace(/^\\/+|\\/+$/g, '').replace(/[^a-zA-Z0-9]+/g, '-').toLowerCase() || 'home';
const markdown = String($json.text || $json.output || '').trim();
const outputMode = $('Prepare Evidence-First Content Brief').item.json.outputMode || 'download';
return { json: { sourceUrl, filename: slug + '.md', outputMode, reviewStatus: 'needs_review' }, binary: { data: { data: Buffer.from(markdown, 'utf8').toString('base64'), mimeType: 'text/markdown', fileName: slug + '.md', fileExtension: 'md' } } };`
    }
  },
  output: [{ json: { sourceUrl: 'https://example.com/page', filename: 'page.md', outputMode: 'download', reviewStatus: 'needs_review' }, binary: { data: { data: 'IyBFeGFtcGxl', mimeType: 'text/markdown', fileName: 'page.md', fileExtension: 'md' } } }]
});

const chooseOutput = node({
  type: 'n8n-nodes-base.if',
  version: 2.3,
  config: {
    name: 'Choose Google Drive or Download',
    parameters: {
      conditions: { options: { caseSensitive: true, leftValue: '', typeValidation: 'strict', version: 2 }, conditions: [{ leftValue: expr('{{ $json.outputMode }}'), rightValue: 'drive', operator: { type: 'string', operation: 'equals' } }], combinator: 'and' }
    }
  },
  output: [{ json: { outputMode: 'drive' } }, { json: { outputMode: 'download' } }]
});

const uploadDrive = node({
  type: 'n8n-nodes-base.googleDrive',
  version: 3,
  config: {
    name: 'Upload Markdown to Google Drive',
    parameters: {
      resource: 'file',
      operation: 'upload',
      authentication: 'oAuth2',
      inputDataFieldName: 'data',
      name: expr('{{ $binary.data.fileName }}'),
      driveId: { __rl: true, mode: 'list', value: 'My Drive' },
      folderId: { __rl: true, mode: 'list', value: 'root', cachedResultName: '/ (Root folder)' },
      simplifyOutput: true
    },
    credentials: { googleDriveOAuth2Api: newCredential('Google Drive account') }
  },
  output: [{ json: { id: 'drive-file-id', name: 'page.md', webViewLink: 'https://drive.google.com/' } }]
});

const returnDownload = node({
  type: 'n8n-nodes-base.respondToWebhook',
  version: 1.5,
  config: {
    name: 'Return Markdown Download',
    parameters: { respondWith: 'binary', responseDataSource: 'set', inputFieldName: 'data', options: { responseCode: 200 } }
  },
  output: [{ json: { downloaded: true }, binary: { data: { data: 'IyBFeGFtcGxl', mimeType: 'text/markdown', fileName: 'page.md', fileExtension: 'md' } } }]
});

export default workflow('sitemap-to-markdown', 'Sitemap to Google-Friendly Markdown Drafts')
  .add(urlIntake)
  .to(fetchSitemap)
  .to(expandUrlSitemap)
  .to(fetchPage)
  .to(preparePrompt)
  .to(generateMarkdown)
  .to(makeFile)
  .to(chooseOutput)
  .add(uploadIntake)
  .to(expandUploadedSitemap)
  .to(fetchPage)
  .add(urlForm)
  .to(fetchSitemap)
  .to(expandFormUrlSitemap)
  .to(fetchPage)
  .add(uploadForm)
  .to(expandFormUploadedSitemap)
  .to(fetchPage)
  .add(combinedForm)
  .to(routeCombinedInput)
  .add(fetchSitemap)
  .to(expandCombinedUrlSitemap)
  .to(fetchPage)
  .add(expandCombinedUploadedSitemap)
  .to(fetchPage)
  .add(uploadDrive)
  .add(returnDownload)
  .add(chooseOutput.output(0).to(uploadDrive))
  .add(chooseOutput.output(1).to(returnDownload))
  .add(routeCombinedInput.output(0).to(fetchSitemap))
  .add(routeCombinedInput.output(1).to(expandCombinedUploadedSitemap));
