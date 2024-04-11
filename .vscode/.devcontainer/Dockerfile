FROM alpine:3.19

ARG USERNAME=default
ARG USER_UID=1000
ARG USER_GID=$USER_UID

RUN apk update && \
    apk upgrade && \
    apk add sudo shadow openssh ffmpeg build-base \
    openssl-dev python3-dev py3-pip postgresql-dev \
    nodejs npm bash git zsh bind-tools

RUN groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
USER $USERNAME

WORKDIR /workspaces/NoiseID/

RUN sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
RUN git clone https://github.com/zsh-users/zsh-autosuggestions ~/.oh-my-zsh/custom/plugins/zsh-autosuggestions && \
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ~/.oh-my-zsh/custom/plugins/zsh-syntax-highlighting && \
sed "s/plugins=(git)/plugins=(git zsh-autosuggestions zsh-syntax-highlighting)/g" >> ~/.zshrc

ENTRYPOINT /bin/zsh
