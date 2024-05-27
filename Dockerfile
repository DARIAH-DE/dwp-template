ARG LATEX_IMAGE_TAG=3.2
FROM pandoc/latex:$LATEX_IMAGE_TAG

ENV XDG_DATA_HOME=/dwp-data

RUN mkdir -p $XDG_DATA_HOME/pandoc/templates $XDG_DATA_HOME/pandoc/csl
COPY DWP.latex $XDG_DATA_HOME/pandoc/templates
COPY *.csl $XDG_DATA_HOME/pandoc/csl
COPY img/* /opt/texlive/texmf-local/tex/latex/local
COPY dwp.py /usr/local/bin 
RUN apk add --update fontconfig font-iosevka-base font-urw-base35 python3
COPY fonts/*.ttc /usr/share/fonts
RUN  tlmgr install koma-script palatino mathpazo; \
  luaotfload-tool --update -vvv

ENTRYPOINT ["/usr/local/bin/dwp.py"]
