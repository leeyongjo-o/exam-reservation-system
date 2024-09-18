FROM postgres:15.8

RUN echo "\n**** setup locale and timezone ****\n"

# make locale data
RUN localedef -i ko_KR -c -f UTF-8 -A /usr/share/locale/locale.alias ko_KR.UTF-8
RUN locale -a | grep ko

# setup locale env.
RUN echo "export LC_ALL='ko_KR.utf8'" >> /etc/profile && \
    echo "export LANG='ko_KR.utf8'" >> /etc/profile && \
    echo "export LANGUAGE='ko_KR.utf8'" >> /etc/profile
ENV LANG ko_KR.utf8

# setup timezone env.
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN echo "Asia/Seoul" > /etc/timezone
ENV TZ Asia/Seoul
