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



Mini MapReduce Framework for Student Subject Dataset
Project Overview

This project implements a Mini MapReduce Framework in Python to process a student subject dataset. The framework simulates the working of Hadoop MapReduce by dividing the data into different stages: splitting, mapping, partitioning, sorting, and reducing. The project counts the number of students enrolled in each subject and generates the final result automatically.

The dataset contains subject names such as Commerce, Computer, English, Maths, Science, and Social. The framework processes these records efficiently and produces the total count for each subject.

Dataset Description

The input dataset is stored in input.txt. Each record represents a student's subject. The first line contains the header, and the remaining lines contain subject names.

Sample Input
Subject
Commerce
Computer
English
Maths
Science
Social
Computer
Maths
English
Science
...

The dataset contains records for the following subjects:

Commerce
Computer
English
Maths
Science
Social
Project Objectives
To simulate the Hadoop MapReduce framework using Python.
To process student subject records.
To count the total number of records for each subject.
To understand the stages of MapReduce.
To generate summarized output from large datasets.
Project Structure
MiniMapReduce/
│── master.py
│── splitter.py
│── mapper.py
│── partition.py
│── sorter.py
│── reducer.py
│── input.txt
│
├── intermediate/
│
└── output/
    └── result.txt
Module Description
master.py

The main program that controls the complete execution of the Mini MapReduce Framework. It reads the dataset and executes all MapReduce stages in sequence.

splitter.py

Splits the input dataset into smaller files for processing. This simulates distributing data among multiple mapper processes.

mapper.py

Reads each subject from the dataset and converts it into a key-value pair.

Example:

Maths
English
Science

becomes

(Maths,1)
(English,1)
(Science,1)
partition.py

Distributes the mapper output into different partition files using hash partitioning so that identical keys reach the same reducer.

sorter.py

Sorts the intermediate key-value pairs alphabetically before they are processed by the reducer.

reducer.py

Groups identical subject names and calculates their total count. The final result is stored in output/result.txt.

Workflow
Read the student subject dataset.
Split the dataset into smaller files (optional).
Execute the Mapper to generate key-value pairs.
Partition the intermediate data.
Sort each partition.
Reduce the sorted data by counting identical subjects.
Store the final output in output/result.txt.
Execution

Run the following command:

python master.py
Output

The program generates the following output:

========== MapReduce Completed ==========
Commerce : 12
Computer : 19
English : 19
Maths : 19
Science : 19
Social : 12

This output indicates the number of occurrences of each subject in the dataset.

Technologies Used
Python 3
Visual Studio Code
File Handling
Hash Partitioning
Sorting
MapReduce Programming Model
Applications
Student subject analysis
Educational data processing
Record counting
Large-scale text processing
Learning the MapReduce programming model
Conclusion

This Mini MapReduce Framework successfully processes the student subject dataset by implementing the core phases of MapReduce. It reads the input records, generates intermediate key-value pairs, partitions and sorts the data, and finally counts the occurrences of each subject. The project demonstrates how large datasets can be processed efficiently using the MapReduce approach and provides a practical understanding of distributed data processing concepts.
