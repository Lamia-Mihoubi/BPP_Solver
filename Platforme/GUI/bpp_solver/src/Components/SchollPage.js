import React from "react";
import Typography from "@material-ui/core/Typography";
import Container from "@material-ui/core/Container";
import ChooseMthd from "./ChooseMthd";
import { withStyles } from "@material-ui/core/styles";
import ShowResults from "./ShowResults";
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';

class SchollPage extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      display_choosemthd: 1,
      display_showresults: 0,
      solutions: "",
      n:0,
      c:0,
      opt:0

    };
    this.handleValider = this.handleValider.bind(this);
    this.handleretour = this.handleretour.bind(this);
  }

  handleValider(solution,n,c,opt) {
    this.setState({
      solutions: solution,
      display_choosemthd: 0,
      display_showresults: 1,
      n:n,
      c:c,
      opt:opt,
    });
  }
  handleretour() {
    this.setState({
      display_choosemthd: 1,
      display_showresults: 0,
    });
  }

  render() {
    const classes = this.props;
    let content;
    
    if (this.state.display_choosemthd) {
      content = (
        <div>
          
          <ChooseMthd
            pagenum={3}
            handleValider={this.handleValider}
          ></ChooseMthd>
        </div>
      );
    }
    if (this.state.display_showresults) {
      // when backend is done change to solutions={this.state.solutions}
      content = (
        <div>
          <Grid container  spacing={3}>
            <Grid item xs={3}>
              <Paper className={classes.paper}>Nombre d'objets: {this.state.n}  </Paper>
            </Grid>
            <Grid item xs={3}>
              <Paper className={classes.paper}>Capacité: {this.state.c}  </Paper>
            </Grid>
            <Grid item xs={4}>
      <Paper className={classes.paper}>Solution optimale: {this.state.opt}</Paper>
            </Grid>
          </Grid>
        <ShowResults
          ecart= {true}
          solutions={this.state.solutions}
          handleretour={this.handleretour}
        ></ShowResults>
        </div>
      );
    }
    return (
      <Container>
       
        
        <div className={classes.empty}></div>
        {content}
      </Container>
    );
  }
}
const styles = (theme) => ({
  root: {
    //backgroundColor: '#020F59',
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    background: 'blue',
    height : 100,
  },
  pagetitle: {
    margin: theme.spacing(1),
  },
  empty: {
    height: "9vw",
  },
});

export default withStyles(styles)(SchollPage);
