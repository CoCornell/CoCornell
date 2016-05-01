/*
AllLists
  - List
    - ListName
    - AllCards
      - Card
      - Image
        - ModalImage
        - ModalText
*/

var AllLists = React.createClass({
  getInitialState: function() {
    return {lists: []};
  },
  loadListsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      success: function(data) {
        this.setState({lists: data.lists});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadListsFromServer();
    setInterval(this.loadListsFromServer, this.props.pollInterval);
  },
  render: function() {    
    var rl = this.removeList;
    var lists = this.state.lists.map(function(list) {
      return (
        <List key={list.id} list={list} removeList={rl} />
      )
    });
    return (
      <div className="allLists">
        {lists}
      </div>
    )
  }
});


var List = React.createClass({
  deleteThisList: function() {
    var list_id = this.props.list.id;
    var r = confirm("Are you sure want to delete this list?");
    if (r) {
      $.ajax({
        url: "/list/" + list_id + "/",
        type: "delete",
        success: function() {
        },
        error: function(xhr, status, err) {
          console.error(this.props.url, status, err.toString());
        }.bind(this)
      });
    }
  },
  render: function() {
    return (
      <div className="list" id={'list' + this.props.list.id}>
        <div className="listName">
          <h4>{this.props.list.name}
            <span className="delete" id={'delete_list' + this.props.list.id} onClick={this.deleteThisList}>&times;</span>
          </h4>
        </div>
        <AllCards url={"/list/" + this.props.list.id + "/"} pollInterval={1000} />
      </div>
    )
  }
});


var AllCards = React.createClass({
  getInitialState: function() {
    return {cards: []};
  },
  loadCardsFromServer: function() {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      success: function(data) {
        if (data.list) {
          this.setState({cards: data.list.cards});
        }
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadCardsFromServer();
    setInterval(this.loadCardsFromServer, this.props.pollInterval);
  },
  render: function() {
    var cards = this.state.cards.map(function(card) {
      if (!card.is_image) {
        return (
          <Card key={card.id} card={card} />
        )
      } else {
        return (
          <Image key={card.id} card={card} />
        )
      }
    });
    return (
      <div className="allCards">
        {cards}
      </div>
    )
  }
});


var Card = React.createClass({
  deleteThisCard: function() {
    var card_id = this.props.card.id;
    $.ajax({
        url: "/card/" + card_id + "/",
        type: "delete",
        success: function() {
        },
        error: function(xhr, status, err) {
          console.error(this.props.url, status, err.toString());
        }.bind(this)
    });
  },
  render: function() {
    return (
      <div className="card">
        <p><span className="delete" id={"delete_card" + this.props.card.id } onClick={this.deleteThisCard}>&times;</span></p>
        <p className="content">{this.props.card.content}</p>
      </div>
    )
  }
});


var Image = React.createClass({
  getInitialState: function() {
    return {showingImage: true};
  },
  render: function() {
    return (
      <div className="image">
        <img className="image" id={"image" + this.props.card.id} 
             src={ "/static/uploads/" + this.props.card.content } 
             alt={ this.props.card.content } 
             data-toggle="modal"
             data-target={ "#modal" + this.props.card.id } 
             data-image-name={ this.props.card.content } />

        <div className="modal fade" id={"modal"+this.props.card.id} tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
            <div className="modal-dialog" role="document">
                <div className="modal-content">
                    <div className="modal-header">
                        <button type="button" className="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
                        <h4 className="modal-title" id="myModalLabel">{ this.props.card.content }</h4>
                    </div>
                    <div className="modal-body">
                      <ModalImage card={this.props.card} />
                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn btn-primary btn-show" id={"show" + this.props.card.id } data-image-name={this.props.card.content}>
                            Show OCR Text
                        </button>
                        <button type="button" className="btn btn-default btn-delete-image" data-dismiss="modal" id={"delete" + this.props.card.id }>
                            Delete
                        </button>
                    </div>
                </div>
            </div>
        </div>
      </div>
    )
  }
});


var ModalImage = React.createClass({
  render: function() {
    return (
      <img className='modal-image' src={"/static/uploads/" + this.props.card.content} />
    )
  }
});


var ModalText = React.createClass({
  getInitialState: function() {
    return {text: ''};
  },
  loadOCRTextFromServer: function() {
    $.ajax({
      url: "/card/" + this.props.card.id + "/ocr-text/",
      type: "GET",
      dataType: "json",
      success: function(data) {
          this.setState({text: data.ocr.text});
          this_button.text("Show Image");
      },
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  componentDidMount: function() {
    this.loadOCRTextFromServer();
  },
  render: function() {
    return (
      <p>{this.state.text}</p>
    )
  }
});


ReactDOM.render(
  <AllLists url="/board3/8/" pollInterval={1000} />,
  document.getElementById('main_board')
);
