$( document ).ready(function() {
  $('.dropdown-button').dropdown({
   inDuration: 300,
   outDuration: 225,
   constrainWidth: false,
   hover: false,
   gutter: 10,
   belowOrigin: true,
   alignment: 'right',
   stopPropagation: false
   }
  );
  $('.tags').material_chip();
  $('.tags-placeholder').material_chip({
    secondaryPlaceholder: 'Add a Tag',
  });

  $('.tags').on('chip.add', function(e, chip){
    $('#id_post_tags').val(function(){
      return this.value + ', ' + chip.tag;
    });
  });
  $('.chips').on('chip.delete', function(e, chip){
    $('#id_post_tags').val(function(){
      return (this.value).replace(chip.tag,'');
    });
  });
  $('.post_delete').dropdown({
   inDuration: 300,
   outDuration: 225,
   constrainWidth: false,
   hover: false,
   gutter: 20,
   belowOrigin: true,
   alignment: 'right',
   stopPropagation: false
   }
  );
});
