FROM node:14.17.1
ENV APPNAME="cwtlbot-discord"
ENV VERSION="0.1.1"
RUN wget https://github.com/DonaldKellett/${APPNAME}/archive/refs/tags/v${VERSION}.tar.gz
RUN tar xvf v${VERSION}.tar.gz && rm v${VERSION}.tar.gz
RUN mv ${APPNAME}-${VERSION} app
WORKDIR /app
RUN npm install
COPY cwtlbot-discord.docker.sh /app/run.sh
CMD ["/app/run.sh"]
