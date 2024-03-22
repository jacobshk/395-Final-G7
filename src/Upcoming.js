import React from 'react';
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemText from '@mui/material/ListItemText';

// TEMPORARY
const assignments = [
  ['2024-03-22', 'Homework 1'],
  ['2024-03-25', 'Quiz 1'],
];

// Assuming the format of each assignment is [date, name], Sort system as well.
const Upcoming = () => {
    const sortedAssignments = assignments.sort((a, b) => new Date(a[0]) - new Date(b[0]));
  
    return (
      <List>
        {sortedAssignments.map(([date, name], index) => (
          <ListItem key={index}>
            <ListItemText
              primary={`${name.substring(0, 20)}${name.length > 20 ? '...' : ''}`}
              secondary={new Date(date).toLocaleDateString()}
            />
          </ListItem>
        ))}
      </List>
    );
  };
  
  export default Upcoming;