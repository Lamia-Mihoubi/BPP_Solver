import React from 'react'
import clsx from 'clsx'
import { Switch, Route, BrowserRouter } from 'react-router-dom'
import CssBaseline from '@material-ui/core/CssBaseline'
import Drawer from '@material-ui/core/Drawer'
import Container from '@material-ui/core/Container'
import Typography from '@material-ui/core/Typography'
import MainContent1 from './MainContent1'
import SideMenu from './SideMenu'
import SchollPage from './SchollPage'
import Samples from './Samples'
import { withStyles } from "@material-ui/core/styles";

class Main extends React.Component{
    constructor(props) {
        super(props)
        this.state={
            panelIndex : 0
        }
        this.handler = this.handler.bind(this)

      }  
    handler(i)  {
        this.setState({
          panelIndex : Number(i)
        });
      }
      
    render(){
        const { classes } = this.props;        
        return (
            <BrowserRouter>
            <div className={clsx('App', classes.root)}>
              <CssBaseline />
              
              <Drawer
                variant="permanent"
                classes={{
                  paper: classes.drawerPaper,
                }}
              >
                <SideMenu handler={this.handler} />
              </Drawer>
            
              <main className={classes.content}>
                <Container maxWidth="lg" className={classes.container}>
                    <MainCont panelIndex={this.state.panelIndex} ></MainCont>
                </Container>
              </main>
            </div>
          </BrowserRouter>
        );
      
        
    }}
    class MainCont extends React.Component{ 
          
    render(){
        const s= this.props.panelIndex 
         const panels = [
            <MainContent1 />,
            <Samples />,
            <SchollPage />,
        ]; 
        const correctPanel = panels[s];
        return (
            <div className="panel-box">
            {correctPanel}
            </div>
        );
    }
    }
    const drawerWidth = 240
    
    const styles = theme => ({
        root: {
            display: 'flex',
          },
          drawerPaper: {
            position: 'relative',
            whiteSpace: 'nowrap',
            width: drawerWidth,
            paddingTop: theme.spacing(4),
            paddingBottom: theme.spacing(4),
            background: '#535454',
            color: '#fff',
          },
          content: {
            flexGrow: 1,
            height: '100vh',
            overflow: 'auto',
          },
          container: {
            paddingTop: theme.spacing(4),
            paddingBottom: theme.spacing(4),
          },
          AppBar : {
            textAlign: 'center'
          
          }
    })  
export default withStyles(styles)(Main);
    