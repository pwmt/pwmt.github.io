title: zathura
description: a document viewer

zathura is a highly customizable and functional document viewer. It provides a
minimalistic and space saving interface as well as an easy usage that mainly
focuses on keyboard interaction.

## Main features

<div class="features">
  <div class="row">
    <div class="col-xs-8">
    <h3>Choose your supported file formats</h3>
    <p>
      You only want to view PDF documents? How about PostScript or DjVu? All
      together?  zathura now uses a <a href="plugins">plugin</a> based system for supported
      document types which makes it possible for you to choose which file formats
      you want your version of zathura to support. This also makes it possible to
      use different backends for the same document type: For instance we provide a
      plugin for PDF documents using either the poppler or the mupdf library.
      </p>
    </div>
    <div class="col-xs-4">
      <img class="img-responsive" src="/static/img/icon-documents.png" alt="Multiple file formats" />
    </div>
  </div>

  <div class="row">
    <div class="col-xs-4">
      <img class="img-responsive" src="/static/img/icon-keyboard.png" alt="LaTeX support" />
    </div>
    <div class="col-xs-8">
      <h3>Mouse-free navigation</h3>
      <p>
        zathura makes it possible to completely view and navigate through
        different documents without using a mouse. Functions to scroll or zoom are
        mapped to certain keys as well as the possibility to follow or open links
        that are shown in the document. By simply pressing the "f" key on your
        keyboard, zathura highlights all links shown on the current screen. By
        typing one of the shown numbers you can easily follow links to chapters or
        open them with your favourite web browser. But of course... you still can
        use the mouse as well.
      </p>
    </div>
  </div>

  <div class="row">
    <div class="col-xs-8">
      <h3>SyncTeX support</h3>
      <p>
        The Synchronization TeXnology named SyncTeX is a new feature
        allows to synchronize between input and output, which means to
        navigate from the source document to the typeset material and vice
        versa. zathura supports that feature in both directions and makes
        writing LaTeX documents even more fun!
      </p>
    </div>
    <div class="col-xs-4">
      <img class="img-responsive" src="/static/img/icon-science-book.png"
      alt="SyncTeX support" />
    </div>
  </div>

  <div class="row">
    <div class="col-xs-4">
      <img class="img-responsive" src="/static/img/icon-bookmarks.png"
      alt="Bookmarks" />
    </div>
    <div class="col-xs-8">
      <h3>Quickmarks and bookmarks</h3>
      <p>
        Whenever you want to find a certain page of the document later on you can use
        bookmarks which are saved by using the command ":bmark". You can easily move to
        your saved bookmarks with the ":blist" command or delete them with ":bdelete".
        Or you can simply use quickmarks. A quickmark is simply a page assigned to a
        letter or number and can therefore saved or opened with only two key presses. To
        create a new quickmark just type "m" followed by a letter or number. To view a
        saved quickmark just use "'" and then the previously used letter or number.
      </p>
    </div>
  </div>

  <div class="row">
    <div class="col-xs-8">
      <h3>Automatic document reloading</h3>
      <p>
      Whenever the file that you are currently looking at changes (e.g.: you are
      working heavily on a LaTeX document and you compile it to view the changes),
      zathura automatically detects that and reloads the document without any
      hesitation.
      </p>
    </div>
    <div class="col-xs-4">
      <img class="img-responsive" src="/static/img/icon-reload.png" alt="LaTeX support" />
    </div>
  </div>

  <div class="row">
    <div class="col-xs-4">
      <img class="img-responsive" src="/static/img/icon-lego.png"
      alt="Lego bricks" />
    </div>
    <div class="col-xs-8">
      <h3>Easily customizable!</h3>
      <p>
        You are not happy with the shortcuts we are providing? You don't like
        the colors? No problem and no worries. Almost everything in zathura is
        easily customizable with a configuration file. If you want to learn
        more, checkout the documentation 
      </p>
    </div>
  </div>

  <div class="row">
    <div class="col-xs-8">
      <h3>... and many more!</h3>
      <p>
        In addition to the above features zathura is capable of exporting images
        and attachments, opening encrypted documents and printing them. You can
        search through the document or browse its index or checkout the document
        meta information. We offer an optional <a
        href="http://sqlite.org">sqlite</a> database backend and we support the
        <a href="https://tools.suckless.org/tabbed/">tabbed</a> tool.
      </p>
    </div>
    <div class="col-xs-4">
      <img class="img-responsive" src="/static/img/icon-puzzle.png" alt="Puzzle" />
    </div>
  </div>
</div>
