import React from 'react'
import Toolbar from '@material-ui/core/Toolbar'
import Typography from '@material-ui/core/Typography'
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles((theme) => ({
    root: {
      position: 'fixed',
      bottom: theme.spacing(2),
      right: theme.spacing(2),
    },
  }));

class NavBar extends React.Component {
    
    render(){
        return (
            <Toolbar>
                <Typography variant="title" color="inherit">
                Navigation Bar lllllllllllllldjlkfjsdlkfjsldkfjskldfjskldfj
                </Typography>
            </Toolbar>
        );
    }
}
export default NavBar;