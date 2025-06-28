FROM alpine:3.17

RUN apk add --no-cache curl

COPY policies/ /policies/

EXPOSE 8181

CMD ["/opa", "run", "--server", "--log-level=info", "/policies"]