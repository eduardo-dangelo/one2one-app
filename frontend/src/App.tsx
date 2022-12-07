import React, {useEffect, useState} from 'react'
import {Box, Typography} from '@mui/material'
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom'
import axios from 'axios'
import SiteHeader from "./common/SiteHeader";
import WorkspaceList from "./common/WorkspaceList";
import useWorkspace from "./hooks/useWorkspace";

function App() {
  const { workspaces } = useWorkspace()
  console.log('workspaces', workspaces)
  return (
    <Router>
      <Box sx={{ display: 'flex', height: '100vh' }}>
        <Box flex={1}>
          <SiteHeader/>
          <WorkspaceList/>
        </Box>
      </Box>
    </Router>
  )
}

export default App
