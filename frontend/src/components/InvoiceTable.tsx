import React, { useEffect, useState } from "react";
import axios from "axios";

const InvoiceTable = () => {
  const [invoices, setInvoices] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:5000/api/invoices").then((res) => setInvoices(res.data));
  }, []);

  return (
    <table>
      <thead><tr><th>ID</th><th>Date</th><th>Amount</th></tr></thead>
      <tbody>
        {invoices.map((inv) => (
          <tr key={inv.id}>
            <td>{inv.id}</td>
            <td>{inv.date}</td>
            <td>${inv.amount}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default InvoiceTable;