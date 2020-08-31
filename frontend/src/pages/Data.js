import React, { useEffect, useState } from "react";
import axios from "axios";
import { Table } from "antd";
import moment from "moment";

export default function Data() {
  const [zyklusZeit, setZyklusZeit] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);
    // axios.get("localhost:8000/time_series/").then(({ data }) => {
    axios.get("http://127.0.0.1:8000/time_series/").then(({ data }) => {
      setIsLoading(false);
      console.log(data);
      setZyklusZeit(data);
    });
  }, []);

  return (
    <Table dataSource={zyklusZeit} columns={columns} loading={isLoading} />
  );
}

const columns = [
  {
    title: "Timestamp",
    key: "timestamp",
    render: (record) => {
      // 28.03.2020 19:51:56
      const date = moment(record.timestamp, "DD.MM.YYYY HH:mm:ss");

      return date.format("DD-MM-YYYY HH:mm:ss");
    },
    sorter: (a, b) => {
      const dateA = moment(a.timestamp, "DD.MM.YYYY HH:mm:ss");
      const dateB = moment(b.timestamp, "DD.MM.YYYY HH:mm:ss");

      return dateA - dateB;
    },
  },
  {
    title: "Cycle Time",
    dataIndex: "cycle_time",
    key: "cycle_time",
    sorter: (a, b) => a.cycle_time - b.cycle_time,
  },
];
