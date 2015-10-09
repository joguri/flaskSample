
var app = angular.module('myApp', []);

app.controller('NotesController', ["$scope", "$http", function($scope, $http) {
    var self = this;
    self.value = "Value From Angular";
    self.dateStr = "Today";
    self.count = 5;
    self.noteContent = "";
    self.titleContent = "";
    self.allData = [];
    self.currentId = "Hi";

    self.updateState = function(id, state) {
        for (var ii in self.allData) {
            rec = self.allData[ii];
            if (rec._id['$oid'] == id) {
                rec.state = state;
                $http.put('/note/'+id, rec).then(function(result) {
                }, function(err) {
                    alert("Update failed", err.toString());
                }).then(function(result) {
                    self.pressHereTapped(null);
                });
            }
        }
        $http.get('/note/' + id).then(function(record) {
            record.state = state;
            return $http('/note/'+id, record, method='UPDATE');
        }).then(function(result) {
            return result;
        });
    }

    self.showEdit = function(event) {
         var epad = $("#editPad");
         var noteList = $("#noteList");
         if (epad.css("opacity") == "1") {
             epad.animate({height:"0px", opacity:0}, 400);
             noteList.animate({opacity:1}, 400);
         } else {
             epad.animate({height:"280px", opacity:1}, 400);
             noteList.animate({opacity:0}, 400);
         }
    }

    self.addNote = function(event) {
        record = {};
        record.title = self.titleContent;
        record.content = self.noteContent;
        record.type = "note";
        record.state = "defined";
        record.details = ""
        $http.post('/note/', record).
            then(function(resp) {
            console.log(resp.data);
            return $http.get('/note');
        }).then(function(resp) {
            self.allData = resp.data;
            self.noteContent = "";
            self.count = self.allData.length;
        });
    };

    self.pressHereTapped = function(event) {
        $http.get('/note').then(function(resp) {
            console.log(resp.data);
            self.allData = resp.data;
        });
    };

    self.deleteTapped = function(id) {
        $http.delete('/note/' + id).then(function(resp) {
            console.log("I think we deleted " + id);
            return $http.get('/note');
        }).then(function(resp) {
            self.allData = resp.data;
            self.currentId = "";
            self.count = self.allData.length;
        });
    };
    self.pressHereTapped(null);

}]).config(function($interpolateProvider) {
    $interpolateProvider.startSymbol('<[');
    $interpolateProvider.endSymbol(']>');
});
