FROM alpine:edge
RUN apk upgrade -U -l && \
    apk --update add squid python && \
    rm -rf /tmp/src && \
    rm -rf /var/cache/apk/*

ADD ./squid.conf /etc/squid/squid.conf
ADD ./auth.py /etc/squid/auth.py
ADD ./splash.py /etc/squid/splash.py
ADD ./landingPage.html /usr/share/squid/errors/templates/landingPage.html
ADD ./start.sh /start.sh

RUN chown -R squid:squid /etc/squid
RUN chown -R squid:squid /usr/share/squid/errors/templates/landingPage.html
RUN chmod u+x /start.sh
RUN chmod u+x /etc/squid/*.py

#VOLUME ["/cache"]

EXPOSE 3128 

CMD ["/start.sh"]
