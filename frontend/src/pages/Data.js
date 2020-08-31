import React, { useEffect, useState } from "react";
import axios from "axios";
import { Table } from "antd";
import moment from "moment";

export default function Data() {
  const [zyklusZeit, setZyklusZeit] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  useEffect(() => {
    setIsLoading(true);
    axios.get("http://127.0.0.1:8000/time_series/").then(({ data }) => {
      setIsLoading(false);

      setZyklusZeit(data);
    });
  }, []);

  return (
    <Table
      rowKey={"id"}
      dataSource={zyklusZeit}
      columns={columns}
      loading={isLoading}
      pagination={{ pageSize: 20 }}
    />
  );
}

const columns = [
  {
    title: "Timestamp",
    render: (record) => {
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
    sorter: (a, b) => a.cycle_time - b.cycle_time,
  },
];
