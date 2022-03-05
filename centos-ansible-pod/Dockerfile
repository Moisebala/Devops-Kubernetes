FROM centos:7
LABEL authors="Moussa Balla"

# setup some system required environment variables
ENV TIMEZONE           "America/New_York"
ENV TERM                xterm-color
ENV NCURSES_NO_UTF8_ACS 1
ENV LC_ALL              C
ENV LANG                en_US.UTF-8
ENV container           docker
ENV HISTTIMEFORMAT "%d/%m/%Y %T "
ENV PROMPT_COMMAND      "history -a; history -c; history -r; rhosp_prompt"


# setup charset, language and timezone
RUN echo -e "LANG=en_US.UTF-8\nLC_ALL=C" > /etc/environment && \
    rm -rf /etc/localtime && \
    ln -s /usr/share/zoneinfo/$TIMEZONE /etc/localtime

# setup yum config, activate this line if you want docs for your packages
RUN sed -i -e "s/tsflags=nodocs/#tsflags=nodocs/g" /etc/yum.conf

# Install requirements.
RUN yum makecache fast \
 && yum -y install deltarpm epel-release initscripts git \
 && yum -y update \
 && yum -y install \
      sudo \
      which \
      python3-pip \
      python-pip \
      bash-completion \
 && yum clean all && \
rm -rf /var/cache/yum

RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \
    systemd-remount-fs.service sys-kernel-config.mount \
    sys-kernel-debug.mount sys-fs-fuse-connections.mount
RUN systemctl mask display-manager.service systemd-logind.service
RUN systemctl disable graphical.target; systemctl enable multi-user.target


RUN echo -e "auth required pam_wheel.so use_uid" >> /etc/pam.d/su


# To shutdown systemd in your container correctly we need to use "SIGRTMIN+3"
STOPSIGNAL SIGRTMIN+3

