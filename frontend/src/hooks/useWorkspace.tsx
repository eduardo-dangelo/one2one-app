import axios from "axios";
import {useState} from "react";

type WorkspaceType = {
  title: string
  id: number
  create_at: string
}


export default function useWorkspace() {
  const [workspaces, setWorkspaces] = useState<WorkspaceType[]>([])
  const [workspacesError, setWorkspacesError] = useState(null)

  const getWorkspaces = () => {
    axios
      .get('http://localhost:8000/api/workspaces/')
      .then((res) => {
        console.log('res', res)
        setWorkspaces(res.data)
      })
      .catch((err) => setWorkspacesError(err))
  }

  const createWorkspace = (wkspace: Partial<WorkspaceType>) => {
    axios
      .post("http://localhost:8000/api/workspaces/", wkspace)
      .then(res => getWorkspaces())
      .catch((err) => setWorkspacesError(err))
  }

  const updateWorkspace = (wkspace: Partial<WorkspaceType>) => {
    axios
      .put(`http://localhost:8000/api/workspaces/${wkspace.id}/`, wkspace)
      .then(res => getWorkspaces())
      .catch((err) => setWorkspacesError(err))
  }

  const deleteWorkspace = (wkspace: Partial<WorkspaceType>) => {
    axios
      .delete(`http://localhost:8000/api/workspaces/${wkspace.id}/`)
      .then(res => getWorkspaces());
  };


  return {
    workspaces,
    getWorkspaces,
    createWorkspace,
    updateWorkspace,
    deleteWorkspace,
    workspacesError,
  }
}