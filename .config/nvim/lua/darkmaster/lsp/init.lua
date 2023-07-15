local status_ok, _ = pcall(require, "lspconfig")
if not status_ok then
  return
end

require "darkmaster.lsp.mason"
require("darkmaster.lsp.handlers").setup()
require "darkmaster.lsp.null-ls"
