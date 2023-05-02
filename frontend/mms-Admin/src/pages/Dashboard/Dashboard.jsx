import React from 'react';

import { Outlet } from 'react-router-dom';

import Navbar from '../../components/Dashboard/Navbar';

import Sidebar from '../../components/Dashboard/Sidebar';

import ProfileSavedModal from '../../components/Modals/ProfileSaved';

import TasksModal from '../../components/Modals/TasksModal';

import NewTasksModal from '../../components/Modals/NewTaskModal';

function Dashboard() {
  return (
    <>
      <ProfileSavedModal />

      <TasksModal />
      <NewTasksModal />

      <div className="w-full h-screen font-mukta overflow-y-auto scroll">
        <Navbar />

        <div className="relative left-0 right-0 bottom-0 top-14 md:top-20">
          <Sidebar />

          <div className="absolute md:left-[20%] w-full md:w-[80%] h-screen p-5">
            <Outlet />
          </div>
        </div>
      </div>
    </>
  );
}

export default Dashboard;
