/*
AllLists
  - List
    - ListName
    - AllCards
      - Card
      - Image
        - ModalImage
        - ModalText
    - AddCardForm
    - AddImageForm
  - AddListForm
*/


var tokens = window.location.href.split("/");
var board_id = tokens[tokens.length-2];


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
  handleAddListSubmit: function(payload) {
    $.ajax({
      url: this.props.url,
      dataType: 'json',
      type: 'POST',
      data: payload,
      success: function(data) {
        var lists = this.state.lists;
        var new_lists = lists.concat([data.list]);
        this.setState({lists: new_lists});
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
    var lists = this.state.lists.map(function(list) {
      return (
        <List key={list.id} list={list} />
      )
    });
    return (
      <div className="allLists">
        {lists}
        <div class="clearfix"></div>
        <AddListForm onAddListSubmit={this.handleAddListSubmit} />
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
        <AllCards url={"/list/" + this.props.list.id + "/"} pollInterval={1000} list_id={this.props.list.id} />
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
  handleAddCardSubmit: function(payload) {
    $.ajax({
      url: "/card/",
      dataType: 'json',
      type: 'POST',
      data: payload,
      success: function(data) {
        var cards = this.state.cards;
        var new_cards = cards.concat([data.card]);
        this.setState({cards: new_cards});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  handleAddImageSubmit: function(payload) {
    $.ajax({
      url: "/upload/",
      dataType: 'json',
      type: 'POST',
      data: payload,
      success: function(data) {
        var cards = this.state.cards;
        var new_cards = cards.concat([data.card]);
        this.setState({cards: new_cards});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
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
        <div className="add">
          <AddCardForm onAddCardSubmit={this.handleAddCardSubmit} list_id={this.props.list_id} />
          <AddImageForm onAddImageSubmit={this.handleAddImageSubmit} list_id={this.props.list_id} />
        </div>
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
  toggle: function() {
    this.setState({showingImage: !this.state.showingImage});
  },
  deleteThisImage: function() {
    $.ajax({
      url: "/card/" + this.props.card.id + "/",
      type: "DELETE",
      dataType: "json",
      success: function(data) {},
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  render: function() {
    var modalBody;
    var buttonText;
    if (this.state.showingImage) {
      modalBody = <ModalImage card={this.props.card} />;
      buttonText = "Show OCR Text";
    } else {
      modalBody = <ModalText card={this.props.card} />;
      buttonText = "Show Image";
    }

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
                      {modalBody}
                    </div>
                    <div className="modal-footer">
                        <button type="button" 
                                className="btn btn-primary btn-show" 
                                id={"show" + this.props.card.id } 
                                data-image-name={this.props.card.content}
                                onClick={this.toggle} >
                            {buttonText}
                        </button>
                        <button type="button" className="btn btn-default btn-delete-image" data-dismiss="modal" onClick={this.deleteThisImage}>
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
      }.bind(this),
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


var AddListForm = React.createClass({
  getInitialState: function() {
    return {name: ''};
  },
  handleNameChange: function(e) {
    this.setState({
      name: e.target.value
    });
  },
  handleSubmit: function(e) {
    e.preventDefault();
    var name = this.state.name.trim();
    if (!name) {
      return;
    }
    this.props.onAddListSubmit({name: name});
    this.setState({name: ''});
    ReactDOM.findDOMNode(this.refs.name).value = "";
  },
  render: function() {
    return (
      <form className="addListForm" onSubmit={this.handleSubmit}>
        <input ref="name" type="text" name="name" onChange={this.handleNameChange} autoComplete="off" required />
        <input type="submit" value="Add list" className="btn btn-primary btn-sm" />
      </form>
    )
  }
});


var AddCardForm = React.createClass({
  getInitialState: function() {
    return {content: ''};
  },
  handleContentChange: function(e) {
    this.setState({
      content: e.target.value
    });
  },
  handleSubmit: function(e) {
    e.preventDefault();
    var content = this.state.content.trim();
    if (!content) {
      return;
    }
    this.props.onAddCardSubmit({
      content: content,
      list_id: this.props.list_id
    });
    this.setState({content: ''});
    ReactDOM.findDOMNode(this.refs.content).value = "";
  },
  render: function() {
    return (
      <form className="addCardForm" onSubmit={this.handleSubmit}>
        <input ref="content" 
               className="content" 
               type="text" 
               name="content" 
               onChange={this.handleContentChange} 
               placeholder="Append a text card"
               autoComplete="off"
               required />
        <input className="add" type="submit" value="Add card" />
      </form>
    )
  }
});


var AddImageForm = React.createClass({
  getInitialState: function() {
    return {
      data_uri: null,
    };
  },
  handleSubmit: function(e) {
    e.preventDefault();
    var data_uri = this.state.data_uri.trim();
    if (!data_uri) {
      return;
    }
    this.props.onAddImageSubmit({
      file: data_uri.substring(21),
      list_id: this.props.list_id
    });
    this.setState({data_uri: ''});
  },
  handleFileChange: function(e) {
    var self = this;
    var reader = new FileReader();
    var file = e.target.files[0];

    reader.onload = function(upload) {
      self.setState({
        data_uri: upload.target.result,
      });
    }

    reader.readAsDataURL(file);
  },
  render: function() {
    return (
      <form ref="uploadForm" className="upload" action="/upload/" method="post" encType="multipart/form-data" onSubmit={this.handleSubmit}>
        <div className="file-upload btn btn-primary btn-sm">
            <span>Choose Image</span>
            <input ref="file" type="file" name="file" className="upload" onChange={this.handleFileChange} />
        </div>
        <input type="submit" value="Upload" className="btn btn-default btn-sm" />
      </form>
    )
  }
});


ReactDOM.render(
  <AllLists url={"/board/" + board_id + "/list/"} pollInterval={1000} />,
  document.getElementById('main_board')
);
