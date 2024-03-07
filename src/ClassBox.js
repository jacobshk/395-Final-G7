import * as React from 'react';
import Box from '@mui/material/Box';
import Link from '@mui/material/Link';
import './ClassBox.css';

export default function AddClassBox() {
  return (
    <Box
      id="class"
      my={4}
      display="flex"
      alignItems="center"
      gap={10}
      p={15}
      sx={{ flexWrap: 'wrap'}}
    >
      
    <div class="main-container">
        <div class="top-container">
            <div class="top-text">
                <Link href="/class-1/class-page/student" color="inherit" underline="none">
                    {'Class 1'}
                </Link>
            </div>
        </div>
        <div class="bottom-container"> 
            <div class="bottom-text">
                Professor
            </div>
        </div>
    </div>
    
    </Box>
    
  );
}