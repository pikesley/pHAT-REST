run:
	foreman start

install:
	sudo pip install -r requirements.txt

lint:
	flake8 *py

clean:
	find . -name "*pyc" -delete

foreman: install
	rm -fr /tmp/phat-rest
	mkdir /tmp/phat-rest
	foreman export -a phat-rest -u pi systemd /tmp/phat-rest
	sudo rsync -av /tmp/phat-rest/ /etc/systemd/system/
	sudo systemctl daemon-reload
	sudo systemctl restart phat-rest.target
