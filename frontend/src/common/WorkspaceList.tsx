import React, {useEffect, useState} from 'react';
import {Box, Collapse, List, ListItem, ListItemButton, ListItemIcon, ListItemText, Typography} from "@mui/material";
import InboxIcon from '@mui/icons-material/Inbox';
import useWorkspace from "../hooks/useWorkspace";
import AddItem from "./AddItem";
import {TransitionGroup} from "react-transition-group";
import IconButton from "@mui/material/IconButton";
import DeleteIcon from '@mui/icons-material/Delete';

const WorkspaceList = () => {
  const { getWorkspaces, workspaces, createWorkspace, deleteWorkspace } = useWorkspace()

  const handleAddWorkspace = (value: string) => {
    createWorkspace({
      title: value,
    })
  }

  const handleDeleteWorkspace = (id: number) => {
    deleteWorkspace({ id })
  }

  useEffect(() => {
    getWorkspaces()
  }, [])

  return (
    <Box
      sx={{
        p: 3,
      }}
    >
      <Typography >
        WorkSpaces
      </Typography>
      <List>
        <TransitionGroup>
          {workspaces?.map((workspace, index) => {
            return (
              <Collapse key={workspace.id}>
                <ListItem
                  disablePadding
                  secondaryAction={
                    <IconButton edge="end" aria-label="delete" onClick={() => handleDeleteWorkspace(workspace.id)}>
                      <DeleteIcon />
                    </IconButton>
                  }
                >
                  <ListItemButton>
                    <ListItemIcon>
                      <InboxIcon />
                    </ListItemIcon>
                    <ListItemText primary={workspace?.title} />
                  </ListItemButton>
                </ListItem>
              </Collapse>
            )
          })}
          <ListItem>
            <AddItem onSubmit={handleAddWorkspace}/>
          </ListItem>
        </TransitionGroup>
      </List>
    </Box>
  )
};

export default WorkspaceList;