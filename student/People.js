import * as React from 'react';
import Link from '@mui/material/Link';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Title from '../Title';

function preventDefault(event) {
  event.preventDefault();
}

export default function People() {
  return (
    <React.Fragment>
      <Title> Roster </Title>

      <p> Class Name </p>
      <p> Students </p>

    </React.Fragment>
  );
}