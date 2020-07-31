FROM jupyter/datascience-notebook:ea01ec4d9f57
LABEL maintainer="hientrinh.hus@gmail.com"

USER root

WORKDIR /home/jovyan/software

RUN apt-get update && \
    apt-get install -y \
    autoconf \
    zlib1g-dev \
    default-jre \ 
    libncurses5-dev \
    unzip \
    libbz2-dev \
    liblzma-dev ncurses-dev libncurses5-dev libncursesw5-dev \ 
    python3 

RUN echo '**************************************' && \
    echo '*******Installing cutadapt ***********' && \
    echo '**************************************' && \
    python3 -m pip install --user --upgrade cutadapt

RUN echo '**************************************' && \
    echo '*******Installing fastqc   ***********' && \
    echo '**************************************' && \
    wget "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip" && \
    unzip fastqc_v0.11.9.zip && rm fastqc_v0.11.9.zip && \
    cd FastQC && \
    chmod a+x fastqc && \
    cd ..

RUN echo '**************************************' && \
    echo '*******Installing bowtie2   ***********' && \
    echo '**************************************' && \
    wget "https://svwh.dl.sourceforge.net/project/bowtie-bio/bowtie2/2.1.0/bowtie2-2.1.0-linux-x86_64.zip" && \
    unzip bowtie2-2.1.0-linux-x86_64.zip && \
    rm bowtie2-2.1.0-linux-x86_64.zip

RUN echo '***********************************' && \
    echo '*******Installing samtools  *******' && \
    echo '***********************************' && \
    wget "https://sourceforge.net/projects/samtools/files/samtools/1.9/samtools-1.9.tar.bz2" && \
    tar -xvjf samtools-1.9.tar.bz2 && rm samtools-1.9.tar.bz2 && \
    cd samtools-1.9 && autoheader && autoconf -Wno-syntax  && \
    ./configure && make && make install && cd .. 


RUN echo '***********************************' && \
    echo '*******Installing BEDtools  *******' && \
    echo '***********************************' && \
    wget "https://github.com/arq5x/bedtools2/releases/download/v2.29.2/bedtools-2.29.2.tar.gz" && \
    tar -zxvf bedtools-2.29.2.tar.gz && \
    rm bedtools-2.29.2.tar.gz && \
    cd bedtools2 && make && \
    cd ..

RUN echo '***********************************' && \
    echo '*******Installing FASTAptamer******' && \
    echo '***********************************' && \
    wget "https://burkelab.missouri.edu/fastaptamer/FASTAptamer_v1.0.3.zip" && \
    unzip FASTAptamer_v1.0.3.zip && \
    rm FASTAptamer_v1.0.3.zip 

RUN echo '***********************************' && \
    echo '*******Installing ucsc package******' && \
    echo '***********************************' && \
    mkdir faToTwoBit && cd faToTwoBit && \ 
    wget "http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/faToTwoBit" && \
    chmod a+x faToTwoBit && \
    cd ..

RUN mkdir twoBitToFa && cd twoBitToFa && \ 
    wget "http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/twoBitToFa" && \
    chmod a+x twoBitToFa && \
    cd ..

RUN echo '***********************************' && \
    echo '*******Installing Velvet     ******' && \
    echo '***********************************' && \
    wget "https://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz" && \
    tar zxvf velvet_1.2.10.tgz && \
    rm velvet_1.2.10.tgz && \
    cd velvet_1.2.10 && \
    make && cd .. 

ENV PATH "$PATH:/home/jovyan/.local/bin/"
ENV PATH "$PATH:/home/jovyan/software/FastQC"
ENV PATH "$PATH:/home/jovyan/software/bowtie2-2.1.0"
ENV PATH "$PATH:/home/jovyan/software/samtools-1.9"
ENV PATH "$PATH:/home/jovyan/software/bedtools2/bin"
ENV PATH "$PATH:/home/jovyan/software/FASTAptamer_v1.0.3"
ENV PATH "$PATH:/home/jovyan/software/faToTwoBit"
ENV PATH "$PATH:/home/jovyan/software/twoBitToFa"
ENV PATH "$PATH:/home/jovyan/software/velvet_1.2.10"

CMD jupyter lab --allow-root

