import React, { useState } from 'react';
import { Paper, Typography, Box, Dialog, DialogTitle, DialogContent, TextField, Button } from '@mui/material';
import { assignmentsData } from '../AssignmentData';

export default function Assignment() {
  const [open, setOpen] = useState(false);
  /* Use a state to keep track of the edited assignment's details */
  const [editableAssignment, setEditableAssignment] = useState(null);

  const handleClickOpen = (assignment) => {
    setEditableAssignment({ ...assignment }); 
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleUpdate = () => {
    /* Update with API and etc here! */
    console.log('Updated Assignment:', editableAssignment);
    setOpen(false);
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setEditableAssignment((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  return (
    <Box sx={{ padding: 2 }}>
      <Typography variant="h6" gutterBottom>
        Assignments Feed
      </Typography>
      {assignmentsData.map((assignment, index) => (
        <Paper key={index} elevation={3} sx={{ marginBottom: 2, padding: 2, cursor: 'pointer' }} onClick={() => handleClickOpen(assignment)}>
          <Typography variant="subtitle1" component="div">
            {assignment.title}
          </Typography>
          <Typography variant="body2" sx={{ marginLeft: 2 }}>
            Due: {assignment.date}
          </Typography>
          <Typography variant="body2" display="block" sx={{ marginTop: 1 }}>
            {assignment.description.substring(0, 100)}...
          </Typography>
        </Paper>
      ))}
      {editableAssignment && (
        <Dialog open={open} onClose={handleClose} aria-labelledby="assignment-details-title">
          <DialogTitle id="assignment-details-title">Edit Assignment</DialogTitle>
          <DialogContent>
            <TextField
              margin="dense"
              name="title"
              label="Assignment Name"
              type="text"
              fullWidth
              variant="outlined"
              value={editableAssignment.title}
              onChange={handleChange}
            />
            <TextField
              margin="dense"
              name="date"
              label="Due Date"
              type="text"
              fullWidth
              variant="outlined"
              value={editableAssignment.date}
              onChange={handleChange}
            />
            <TextField
              margin="dense"
              name="type"
              label="Type"
              type="text"
              fullWidth
              variant="outlined"
              value={editableAssignment.type}
              onChange={handleChange}
            />
            <TextField
              margin="dense"
              name="description"
              label="Description"
              multiline
              rows={4}
              fullWidth
              variant="outlined"
              value={editableAssignment.description}
              onChange={handleChange}
            />
            <TextField
              margin="dense"
              name="points"
              label="Points"
              type="text"
              fullWidth
              variant="outlined"
              value={editableAssignment.points}
              onChange={handleChange}
            />
            <Box sx={{ display: 'flex', justifyContent: 'flex-end', mt: 2 }}>
              <Button onClick={handleClose} color="primary">
                Cancel
              </Button>
              <Button onClick={handleUpdate} color="primary" variant="contained" sx={{ ml: 2 }}>
                Update
              </Button>
            </Box>
          </DialogContent>
        </Dialog>
      )}
    </Box>
  );
}