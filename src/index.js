import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import NavBar from './NavBar';
import SClassOverviewNavBar from './student/SClassOverviewNavBar';
import TClassOverviewNavBar from './teacher/TClassOverviewNavBar';
import SignUp from './SignUp'
import SignIn from './SignIn'
import ClassBox from './ClassBox'
import {BrowserRouter, Routes, Route} from 'react-router-dom'
import reportWebVitals from './reportWebVitals';
import SGradebook from './student/SGradebook';
import SAssignment from './student/SAssignment';
import SCalendar from './student/SCalendar';
import SClass from './student/SClass';
import SPeople from './student/SPeople';
import TCalendar from './teacher/TCalendar';
import TClass from './teacher/TClass';
import TAssignment from './teacher/TAssignment';
import TGradebook from './teacher/TGradebook';
import TPeople from './teacher/TPeople';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<><NavBar /></>}/>
        <Route path="/signup" element={<><NavBar /><SignUp /></>}/>
        <Route path="/signin" element={<><NavBar /><SignIn /></>}/>

        <Route path="/home/student" element={<><SClassOverviewNavBar /><ClassBox /></>}/>
        <Route path="/calendar/student" element={<><SCalendar /></>}/>
        <Route path="/class-1/class-page/student" element={<><SClass /></>}/>
        <Route path="/class-1/assignments/student" element={<><SAssignment /></>}/>
        <Route path="/class-1/gradebook/student" element={<><SGradebook /></>}/>
        <Route path="/class-1/people/student" element={<><SPeople /></>}/>

        <Route path="/home/teacher" element={<><TClassOverviewNavBar /><ClassBox /></>}/>
        <Route path="/calendar/teacher" element={<><TCalendar /></>}/>
        <Route path="/class-1/class-page/teacher" element={<><TClass /></>}/>
        <Route path="/class-1/assignments/teacher" element={<><TAssignment /></>}/>
        <Route path="/class-1/gradebook/teacher" element={<><TGradebook /></>}/>
        <Route path="/class-1/people/teacher" element={<><TPeople /></>}/>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
