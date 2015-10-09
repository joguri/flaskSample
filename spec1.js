describe('Controller: NotesController', function() {

    var ctrl, scope, http;

    beforeEach(module('myApp'));

    beforeEach(inject(function($rootScope, $controller) {
        scope = $rootScope.$new();
        ctrl = $controller('NotesController', {$scope : scope});
    }));


    it('should have value available on load', function() {
        expect(ctrl.someData).toEqual(
	        {"name1": "No Action Yet"}
	    );
	 });

    it('should have someData available on load', function() {
        expect(ctrl.value).toEqual("Value From Angular");
	});

});

