FROM elasticsearch:5.5.2-alpine
WORKDIR /opt
COPY docker-compose/elasticsearch/elasticsearch-analysis-ik-5.5.2.zip ./
RUN mkdir /usr/share/elasticsearch/plugins/ik \
    && unzip elasticsearch-analysis-ik-5.5.2.zip \
    && mv elasticsearch/* /usr/share/elasticsearch/plugins/ik \
    && rm elasticsearch-analysis-ik-5.5.2.zip \
    && chown elasticsearch.elasticsearch -R /usr/share/elasticsearch -R
USER elasticsearch
EXPOSE 9200
ENTRYPOINT /usr/share/elasticsearch/bin/elasticsearch