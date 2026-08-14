(function(){
  if (!document.modelContext || typeof document.modelContext.registerTool !== 'function') return;
  document.modelContext.registerTool({
    name: 'openSibeAsk',
    description: 'Open the Sibe natural-language information endpoint for a question about public Sibe CAD resources.',
    inputSchema: {
      type: 'object',
      properties: {
        question: {
          type: 'string',
          description: 'A natural-language question about Sibe cloud CAD management, SolidWorks workflows, trial details, pricing, security, or contact options.'
        }
      },
      required: ['question']
    },
    annotations: {
      readOnlyHint: true,
      destructiveHint: false,
      openWorldHint: false
    },
    execute: async function(args){
      var question = args && args.question ? String(args.question) : '';
      var target = '/ask/' + (question ? '?q=' + encodeURIComponent(question) : '');
      window.location.assign(target);
      return 'Opening the Sibe information endpoint.';
    }
  }).catch(function(){});
})();
