# frontend/Dockerfile (Vite -> nginx)
FROM node:18-alpine AS builder
WORKDIR /app

# Declare build arguments
ARG VITE_CLERK_PUBLISHABLE_KEY
ARG VITE_API_URL

# Set as environment variables for the build
ENV VITE_CLERK_PUBLISHABLE_KEY=pk_test_bmF0aW9uYWwtb3NwcmV5LTk4LmNsZXJrLmFjY291bnRzLmRldiQ
ENV VITE_API_URL=http://localhost:8000

COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build


FROM nginx:stable-alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
