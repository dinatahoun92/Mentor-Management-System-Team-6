/* eslint-disable no-param-reassign */
import { createSlice } from '@reduxjs/toolkit';

const taskSlice = createSlice({
  name: 'tasks',
  initialState: {
    task: [],
    isLoading: false,
    isTaskClicked: false,
    clickedTask: null,
    error: false,
  },
  reducers: {
    // reducers for the login page
    getTaskStart: (state) => {
      state.isLoading = true;
    },
    getTaskSuccess: (state, action) => {
      state.task = action.payload;
      state.error = false;
      state.isLoading = false;
    },
    getTaskFailure: (state) => {
      state.isLoading = false;
      state.error = true;
    },
    taskInfoOpen: (state, action) => {
      state.isTaskClicked = true;
      state.clickedTask = action.payload;
    },
    saveTaskList: (state, action) => {
      state.task = action.payload;
    },
  },
});

export default taskSlice.reducer;
export const {
  getTaskStart,
  getTaskSuccess,
  getTaskFailure,
  taskInfoOpen,
  saveTaskList,
} = taskSlice.actions;
