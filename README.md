# README

This project simulates a **Flipkart real-time log monitoring system** using TCP socket communication.
Three Flipkart regional servers (**Chennai, Bangalore, and Mumbai**) continuously generate logs related to orders, payments, and deliveries.
A **multi-threaded log harvester daemon** collects logs from all servers simultaneously.
The incoming data stream is processed in real time using **socket slicing** techniques.
Each log message is validated using **regular expressions (Regex)**.
Valid logs are converted into **structured payloads** for easy processing.
The logs are dynamically partitioned based on **region and severity level**.
The processed logs are stored in **binary files** for efficient storage and retrieval.
The `read_binary_logs.py` program converts binary files back into readable log messages.
This project demonstrates concepts such as **TCP sockets, multi-threading, regex validation, and binary storage** in the **Flipkart E-Commerce domain**.
