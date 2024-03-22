import * as React from 'react';
import Link from '@mui/material/Link';
import Title from '../Title';

function preventDefault(event) {
  event.preventDefault();
}

export default function Orders() {
  return (
    <React.Fragment>
      <Title> Feed </Title>

      <p> Teacher Name </p>
      <p> Description/Information: </p>
      <p> This is the Information.</p>
      <Link color="primary" href="/class-1/assignments/student" onClick={preventDefault} sx={{ mt: 3 }}>
      See more
      </Link>
    </React.Fragment>
  );
}