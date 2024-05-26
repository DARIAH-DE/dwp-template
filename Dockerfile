ARG LATEX_IMAGE_TAG=latest
FROM pandoc/latex:$LATEX_IMAGE_TAG

RUN mkdir -p /root/.local/share/pandoc
COPY DWP.latex /root/.local/share/pandoc
COPY *.csl /root/.local/share/pandoc
COPY img/* /opt/texlive/texmf-local/tex/latex/local
COPY dwp.py /usr/local/bin 
RUN apk add --update fontconfig font-iosevka-base font-urw-base35 python3
COPY fonts/*.ttc /usr/share/fonts
RUN  tlmgr install koma-script palatino mathpazo; \
  luaotfload-tool --update --force -vvv

ENTRYPOINT ["/usr/local/bin/dwp.py"]
