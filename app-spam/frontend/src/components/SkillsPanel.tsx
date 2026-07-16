import { skills } from "../data/skills";

function SkillsPanel() {

    return (

        <div className="skills-panel">

            <h4 className="skills-title">
                Technical Skills
            </h4>

            {skills.map((group) => (

                <div
                    key={group.category}
                    className="skills-group"
                >

                    <h6 className="skills-category">

                        {group.category}

                    </h6>

                    <div className="skills-badges">

                        {group.skills.map((skill) => (

                            <span
                                key={skill}
                                className="badge bg-primary"
                            >

                                {skill}

                            </span>

                        ))}

                    </div>

                </div>

            ))}

        </div>

    );

}

export default SkillsPanel;