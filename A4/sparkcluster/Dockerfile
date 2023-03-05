FROM ubuntu:20.04

# Install dependencies and libraries for spark
RUN apt-get update && apt-get -y upgrade && apt-get install -y curl vim wget software-properties-common ssh net-tools ca-certificates
RUN apt install -y --fix-missing openjdk-8-jre-headless
RUN apt install -y scala
RUN apt install -y wget
RUN apt install -y screen
RUN apt install -y tzdata
# Install spark
RUN wget https://archive.apache.org/dist/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz \
&& tar xvf spark-3.2.0-bin-hadoop3.2.tgz \
&& mv spark-3.2.0-bin-hadoop3.2/ /usr/local/spark \
&& rm spark-3.2.0-bin-hadoop3.2.tgz
#Set env
ENV SPARK_MASTER_PORT=7077 \
SPARK_MASTER_WEBUI_PORT=8080 \
SPARK_LOG_DIR=/usr/local/spark/logs \
SPARK_MASTER_LOG=/usr/local/spark/logs/spark-master.out \
SPARK_WORKER_LOG=/usr/local/spark/logs/spark-worker.out \
SPARK_WORKER_WEBUI_PORT=8080 \
SPARK_WORKER_PORT=7000 \
SPARK_MASTER="spark://spark-master:7077" \
SPARK_WORKLOAD="master"

ENV PATH="${PATH}:$SPARK_HOME/bin"
ENV SPARK_HOME="/usr/local/spark" \
PYTHONHASHSEED=1
ENV SPARK_NO_DAEMONIZE="true"

EXPOSE 8081 7077 6066

#create log files
RUN mkdir -p $SPARK_LOG_DIR && \
touch $SPARK_MASTER_LOG && \
touch $SPARK_WORKER_LOG && \
ln -sf /dev/stdout $SPARK_MASTER_LOG && \
ln -sf /dev/stdout $SPARK_WORKER_LOG

RUN sleep 15
COPY start-spark.sh /
# Start script
CMD ["/bin/bash", "/start-spark.sh"]
