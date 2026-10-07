FROM node:22-bookworm-slim

RUN npm install --global prism-mcp-server@20.21.17 --omit=dev --no-audit --no-fund

ENV PRISM_STORAGE=local
VOLUME /root/.prism-mcp
ENTRYPOINT ["prism-mcp-server"]
