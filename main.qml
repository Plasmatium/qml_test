import QtQuick 2.5

Rectangle {
	id: root
	width: 800
	height:400
	color: 'steelblue'

	MouseArea {
		anchors.fill: parent
		onClicked: {
			
		}
	}

	Component.onCompleted: {
		//py.log(root)
	}
}